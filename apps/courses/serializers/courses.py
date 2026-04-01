from rest_framework.serializers import ModelSerializer

from apps.courses.models import Course

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "author",
            "banner",
            "name",
            "description",
            "category",
            "country",
            "region",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]