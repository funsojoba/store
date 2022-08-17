from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from helpers.response import Response
from .serializers import (
    StoreSerializer,
)

from .service import StoreService


class StoreViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_description="Create a store",
        operation_summary="Create a store",
        tags=["Store"],
        request_body=StoreSerializer,
    )

    def create(self, request):
        serializer = StoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service_response = StoreService.create_store(request, **serializer.data)

        return Response(data=StoreSerializer(service_response).data, status=status.HTTP_201_CREATED)


    @swagger_auto_schema(
        operation_description="Get all stores",
        operation_summary="Get all stores",
        tags=["Store"],
    )

    def list(self, request):
        service_response = StoreService.get_all_store(request)
        return Response(
            data=dict(
                store=StoreSerializer(service_response, many=True).data), 
            status=status.HTTP_200_OK)

    
    @swagger_auto_schema(
        operation_description="Retrieve a Store",
        operation_summary="Retrieve a store",
        tags=["Store"],
    )

    def retrieve(self, request, pk=None):
        service_response = StoreService.get_store(id=pk)
        
        return Response(
            data=dict(
                store=StoreSerializer(service_response).data), 
            status=status.HTTP_200_OK)

    