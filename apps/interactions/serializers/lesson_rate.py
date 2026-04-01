from rest_framework.serializers import ModelSerializer

from apps.interactions.models import LessonRate

class LessonRateSerializer(ModelSerializer):
    class Meta:
        model = LessonRate
        fields = [
            "id",
            "lesson",
            "user",
            "star_count",
            "comment",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]
