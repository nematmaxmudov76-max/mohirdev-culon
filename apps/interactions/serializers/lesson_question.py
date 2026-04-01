from rest_framework.serializers import ModelSerializer

from apps.interactions.models import LessonQuestion

class LessonQuestionSerializer(ModelSerializer):
    class Meta:
        model = LessonQuestion
        fields = [
            "id",
            "lesson"
            "user",
            "text",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "update_at",
        ]