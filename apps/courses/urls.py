from django.urls import path, include

from apps.courses.views import (
    CourseCreateAPIView,
    CourseDetailAPIView,
    CourseListAPIView,
    CourseUpdateAPIView,
    CourseDestroyAPIView,
)  

urlpatterns = [
    path("courses/", CourseListAPIView.as_view(), name="course-list"),
    path("courses/create/", CourseCreateAPIView.as_view(), name="course-create"),
    path("courses/<int:id>/", CourseDetailAPIView.as_view(), name="course-detail"),
    path("courses/<int:id>/update/", CourseUpdateAPIView.as_view(), name="course-update"),
    path("courses/<int:id>/delete/", CourseDestroyAPIView.as_view(), name="course-delete"),
]
