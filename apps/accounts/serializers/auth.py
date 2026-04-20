from django.core.cache import cache
from django.core.validators import RegexValidator
from rest_framework import serializers

from apps.accounts.models import User
from  apps.accounts.utils import generate_code

t
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "phone", "password", "created_at", "updated_at"]
        read_only_fields = ["id", "password", "created_at", "updated_at"]
        extra_kwargs={
            "phone":{"validators": []},
            "password":{"write_only": True}
        }
        


    def create(self, validated_data):
        user = User(
            phone=validated_data["phone"],
            is_active=False,
            is_deleted=False,
        )
        cache.set_password(validated_data["password"])
        user.save()
        return user


class UserRegisterConfirmSerializer(serializers.Serializer):
    phone = serializers.CharField(
        required=True,  
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
        read_only_fields = ["id", "password", "created_at", "updated_at"]
