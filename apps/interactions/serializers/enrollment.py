from rest_framework.serializers import ModelSerializer

from apps.interactions.models import Enrollment

class EnrollmentSerializer(ModelSerializer):
    class Meta:
        model = Enrollment
        fields = [
            "id",
            "user",
            "course",
            "started_at",
            "finished_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "update_at",
        ]