import uuid
from django.conf import settings
from django.contrib.auth.hashers import check_password

from .models import User

from helpers.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer


class UserService:
    @classmethod
    def create_user(cls, **kwargs):
        password = kwargs.get("password")

        user = User.objects.create(
            first_name=kwargs.get("first_name"),
            last_name=kwargs.get("last_name"),
            email=kwargs.get("email"),
            
        )
        user.set_password(password)
        user.save()
        
        return UserSerializer(instance=user).data

    

    @classmethod
    def login_user(cls, email, password):
        user = cls.get_user(email=email)

        if user:
            user_password = check_password(password, user.password)

            if not user_password:
                return Response(errors={"error": "incorrect password"})

            token = RefreshToken.for_user(user)
            data = {
                "user": UserSerializer(instance=user).data,
                "token": {"refresh": str(token), "access": str(token.access_token)},
            }
            return Response(data=data)
        return Response(errors={"error": "User does not exist"})

    @classmethod
    def get_all_users(cls):
        return User.objects.all()
    
    @classmethod
    def get_user(cls, **kwargs):
        return User.objects.filter(**kwargs).first()
