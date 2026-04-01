from rest_framework.serializers import ModelSerializer
from apps.interactions.models import UserHomeworkAttempt

class UserHomeworkAttempt(ModelSerializer):
    class Meta:
        model = UserHomeworkAttempt
        fields = [
            "id",
            "lesson",
            "user",
            "title",
            "description",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]