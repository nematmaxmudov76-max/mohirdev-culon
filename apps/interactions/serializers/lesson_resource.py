from rest_framework.serializers import ModelSerializer
from apps.interactions.models import LessonResource

class LessonResourceSerializer(ModelSerializer):
    class Meta:
        model = LessonResource
        fields = [
            "id",
            "lesson",
            "media",
            "caption",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]