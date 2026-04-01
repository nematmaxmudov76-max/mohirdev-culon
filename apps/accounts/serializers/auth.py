from django.core.cache import cache
from django.core.validators import RegexValidator
from rest_framework import serializers

from apps.accounts.models import User
from config.utils import generate_sms_code


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "phone", "password", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def save(self, **kwargs):
        user = User(
            phone=self.validated_data["phone"],
            password=self.validated_data["password"],
            is_active=False,
            is_deleted=False,
        )

        user.save()
        code = generate_sms_code()
        cache.set(f"sms_code_{user.id}", code, timeout=300)

        return user


class UserRegisterConfirmSerializer(serializers.Serializer):
    phone = serializers.CharField(
        validators=[RegexValidator(r"^\+?1?\d{9,15}$")],
        max_length=50,
    )
    code = serializers.CharField(max_length=6)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "phone",
            "first_name",
            "last_name",
            "avatar",
            "bio",
            "age",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
