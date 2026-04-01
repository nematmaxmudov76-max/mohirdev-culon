from rest_framework.serializers import ModelSerializer
from apps.interactions.models import LessonAnswer

class LessonAnswearSerializer(ModelSerializer):
    class Meta:
        model = LessonAnswer
        fields = [
            "id",
            "lesson",
            "user",
            "question",
            "text", 
            "is_deleted",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "update_at",
        ]