from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action

from helpers.response import Response
from .serializers import (
    UserSerializer,
    LoginUserSerializer
)

from .service import UserService
# from .docs import schema_example


class AuthViewSet(viewsets.ViewSet):
    @swagger_auto_schema(
        operation_description="Sign up a user",
        operation_summary="Sign up a user",
        tags=["Auth"],
        # responses=schema_example.COMPLETE_REGISTRATION_RESPONSES,
    )
    @action(detail=False, methods=["post"], url_path="signup")
    def user_signup(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service_response = UserService.create_viewer_user(**serializer.data)

        return Response(data=service_response, status=status.HTTP_201_CREATED)


    @swagger_auto_schema(
        operation_description="Login User",
        operation_summary="Login User",
        tags=["Auth"],
        # responses=schema_example.COMPLETE_REGISTRATION_RESPONSES,
        request_body=LoginUserSerializer,
    )
    @action(detail=False, methods=["post"], url_path="login")
    def login(self, request):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service_response = UserService.login_user(
            serializer.data.get("email"), serializer.data.get("password")
        )
        return service_response
