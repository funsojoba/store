from rest_framework import serializers
from authentication.models import User



def validate_exisiting_email(email):
    if User.objects.filter(email=email).exists():
        raise serializers.ValidationError(
                "A user has already registered with this email address"
            )