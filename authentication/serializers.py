from rest_framework import serializers
from .models import User

from authentication.validators import validate_exisiting_email


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    email = serializers.EmailField()

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user:
            raise serializers.ValidationError(detail="User with email already exist.")
        self.user = user.first()
        return value


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class SignupSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200, required=True)
    last_name = serializers.CharField(max_length=200, required=True)
    email = serializers.EmailField(required=True, validators=[validate_exisiting_email])
    password = serializers.CharField(write_only=True, required=True)