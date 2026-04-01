from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from apps.courses.models import Lesson
from apps.courses.serializers import LessonSerializer

class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all().order_by("created_at")
    serializer_class = LessonSerializer

class LessonDetailAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    lookup_field = "id"

class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all().order_by("name")
    serializer_class = LessonSerializer

class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    lookup_field = "id"

class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    lookup_field = "id"