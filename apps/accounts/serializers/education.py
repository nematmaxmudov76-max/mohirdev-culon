from rest_framework.serializers import ModelSerializer

from apps.accounts.models import Education

class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = [
            "id",
            "name",
            "website_url",
            "type",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]