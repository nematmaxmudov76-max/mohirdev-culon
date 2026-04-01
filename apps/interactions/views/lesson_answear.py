from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
)

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from apps.interactions.models import LessonAnswear
from apps.interactions.serializers import LessonAnswearSerializer

class LessonAnswearListAPIView(ListCreateAPIView):
    queryset = LessonAnswear.objects.all().order_by("-created_at")
    serializer_class = LessonAnswearSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class LessonAnswearDetailAPIView(RetrieveAPIView):
    queryset  = LessonAnswear.objects.all()
    serializer_class = LessonAnswearSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

class LessonAnswearCreateAPIView(CreateAPIView):
    queryset = LessonAnswear.objects.all()
    serializer_class = LessonAnswearSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class LessonAnswearDeletedAPIView(DestroyAPIView):
    queryset = LessonAnswear.objects.all()
    serializer_class = LessonAnswearSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

class LessonAnswearUpdateAPIView(UpdateAPIView):
    queryset = LessonAnswear.objects.all()
    serializer_class = LessonAnswearSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
