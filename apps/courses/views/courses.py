from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from apps.courses.models import Course
from apps.courses.serializers.courses import CourseSerializer

class CourseListAPIView(ListAPIView):
    queryset = Course.objects.all().order_by("created_at")
    serializer_class = CourseSerializer

class CourseDetailAPIView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "id"

class CourseCreateAPIView(CreateAPIView):
    queryset = Course.objects.all().order_by("name")
    serializer_class = CourseSerializer

class CourseUpdateAPIView(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "id"
    

class CourseDestroyAPIView(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "id"

    