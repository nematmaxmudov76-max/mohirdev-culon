from django.core.cache import cache
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.generics import (
    GenericAPIView,
    RetrieveAPIView,
)

from apps.accounts.models import User
from apps.accounts.serializers.auth import (
    UserRegisterSerializer,
    UserRegisterConfirmSerializer,
    UserProfileSerializer,
)


class UserRegisterAPIView(GenericAPIView):
    queryset = User.objects.filter(is_active=False, is_deleted=False)
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if User.objects.filter(
            phone=serializer.validated_data["phone"], is_active=True, is_deleted=False
        ).exists():
            return Response(
                {"detail": "User with this phone already exists."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = serializer.save()
        return Response(
            UserRegisterSerializer(user).data, status=status.HTTP_201_CREATED
        )


class UserRegisterConfirmAPIView(GenericAPIView):
    queryset = User.objects.filter(is_active=False, is_deleted=False)
    serializer_class = UserRegisterConfirmSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        phone = request.data.get("phone")
        code = request.data.get("code")
        user = User.objects.filter(
            phone=phone, is_active=False, is_deleted=False
        ).first()

        if not user:
            raise ValidationError("User not found")
        if not cache.get(f"sms_code_{phone}"):
            raise ValidationError("SMS code expired")
        if code != cache.get(f"sms_code_{phone}"):
            raise ValidationError("Invalid SMS code")
        user.is_active = True
        user.save()
        return Response(UserRegisterSerializer(user).data, status=status.HTTP_200_OK)


class UserProfileAPIView(RetrieveAPIView):
    queryset = User.objects.filter(is_active=True, is_deleted=False)
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get_object(self):
        return self.request.user
