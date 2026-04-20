from django.core.cache import cache
from rest_framework import status
from django.db import transaction
from django.utils.crypto import get_random_string
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.generics import (
    GenericAPIView,
    RetrieveAPIView,
)

from apps.accounts.models import User, Wallet
from apps.accounts.serializers.auth import (
    UserRegisterSerializer,
    UserRegisterConfirmSerializer,
    UserProfileSerializer,
)
from apps.accounts.utils import generate_code
from apps.accounts.tasks import sent_sms_to_phone


def _generate_deleted_phone(user_id: int) -> str:
    for _ in range(10):
        candidate = f"{user_id}{get_random_string(8, allowed_chars="'0123456789abcdefghijklmnopqrstuvwxyz")}"[:20]
        if not User.objects.filter(phone = candidate).exists():
            return candidate
    raise ValidationError("Could not generate unique deleted phone value")


class UserRegisterAPIView(GenericAPIView):
    queryset = User.objects.filter(is_active=True, is_deleted=False)
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwrags):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data["phone"]
        password =serializer.validated_data["password"]

        with transaction.atomic():
            user = User.objects.select_for_update().filter(phone = phone).first() 
            if user and user.is_active and not user.is_deleted:

                raise ValidationError("User allaqachon mavjud")

            if user and user.is_deleted:
                user.phone = _generate_deleted_phone(user.pk)
                user.is_active = False
                user.save(update_fields=["phone", "is_active"])
                user = None
            if user is None:
                user = serializer.save()
            else:
                user.set_password(password)
                user.is_active = False
                user.save(update_fields=["password", "is_active"])

        code  = generate_code()
        phone = user.phone.replace("+", "")
        sent_sms_to_phone.delay(phone = phone, message = f"UICdev platformasiga kirish uchun kod: {code}")
        cache.set(f"sms_code{user.phone}", code, 60*2)
        return Response({"message": "telefonga sms yuborildi"})

class UserRegisterConfirmAPIView(GenericAPIView):
    queryset = User.objects.filter(is_active=False, is_deleted=False)
    serializer_class = UserRegisterConfirmSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        
        phone = serializer.validated_data["phone"]
        code = serializer.validated_data["code"]
        user = User.objects.filter(phone = phone, is_deleted=False).first

        if not user:
            raise ValidationError("User not found")
        cached_code = cache.get(f"sms_code_{user.phone}")
        if not cached_code:
            raise ValidateionError("Kod eskirgan yoki mavjud emas")
        if cached_code != cached_code:
            raise ValidationError("Noto'g'ri kod")
        
        with transaction.atomic():
            user.is_active = True
            user.save(update_fields=["is_active"])
            wallet = Wallet.objects.create(user=user)
            Transaction.objects.create(wallet = wallet, amount = 10000) # birinchi ro'yxatdan o'tgan foydalanuvchilarga 10000 so'm bonus beramiz

            


class UserProfileAPIView(RetrieveAPIView):
    queryset = User.objects.filter(is_active=True, is_deleted=False)
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get_object(self):
        return self.request.user
    