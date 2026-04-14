from rest_framework.serializers import ModelSerializer
from apps.notifications.models import Notification

class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            "id",
            "user",
            "course",
            "module",
            "category",
            "title",
            "message",
            "is_send_to_all",
            "image",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "update_at",
        ]