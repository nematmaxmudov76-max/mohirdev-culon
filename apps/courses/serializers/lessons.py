from rest_framework.serializers import ModelSerializer

from apps.courses.models import Lesson

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            "id",
            "module",
            "name",
            "video",
            "description",
            "current_rating",
            "type",
            "lesson_order",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]