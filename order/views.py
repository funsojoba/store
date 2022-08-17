from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from helpers.response import Response
from .serializers import (
    ItemSerializer,
    OrderSerializer,
    CreateOrderSerializer
)

from .service import OrderSerivce, ItemSerivce


class OrderViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_description="Create a order",
        operation_summary="Create a order",
        tags=["Order"],
        request_body=CreateOrderSerializer,
    )

    def create(self, request):
        serializer = CreateOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service_response = OrderSerivce.create_order(request, **serializer.data)

        return Response(data=OrderSerializer(service_response).data, status=status.HTTP_201_CREATED)


    @swagger_auto_schema(
        operation_description="Get all orders",
        operation_summary="Get all orders",
        tags=["Order"],
    )
    @action(
            detail=False, methods=["get"], url_path="(?P<store_id>[a-z,A-Z,0-9]+)"
        )
    def list_order(self, request):
        service_response = OrderSerivce.list_store_order(store_id)
        return Response(
            data=dict(
                store=OrderSerializer(service_response, many=True).data), 
            status=status.HTTP_200_OK)

    
    # @swagger_auto_schema(
    #     operation_description="Retrieve a Store",
    #     operation_summary="Retrieve a store",
    #     tags=["Store"],
    # )

    # def retrieve(self, request, pk=None):
    #     service_response = StoreService.get_store(id=pk)
        
    #     return Response(
    #         data=dict(
    #             store=StoreSerializer(service_response).data), 
    #         status=status.HTTP_200_OK)

    
class ItemViewSet(viewsets.ViewSet):
    permission_classes = []
    
    @swagger_auto_schema(
        operation_description="Get all items",
        operation_summary="Get all items",
        tags=["Item"],
    )

    @action(
        detail=False,
        methods=["get"],
        url_path="list",
    )
    def get_item(self, request):
        service_response = ItemSerivce.get_all_items()
        return Response(
            data=dict(
                store=ItemSerializer(service_response, many=True).data), 
            status=status.HTTP_200_OK)