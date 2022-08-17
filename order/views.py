from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from helpers.response import Response
from .serializers import (
    ItemSerializer,
    OrderSerializer,
    CreateOrderSerializer,
    ItemListSerializer
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
        operation_description="Get all store orders",
        operation_summary="Get all store orders",
        tags=["Order"],
    )
    @action(detail=False, methods=["get"], url_path="(?P<store_id>[a-z,A-Z,0-9]+)/")
    def list_order(self, request, store_id=None):
        service_response = OrderSerivce.list_store_order(store_id=store_id)
        return Response(
            data=dict(
                store=OrderSerializer(service_response, many=True).data), 
            status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        operation_description="Add items to an order",
        operation_summary="Add items to an order",
        tags=["Order"],
    )
    @action(detail=False, methods=["post"], url_path="(?P<order_id>[a-z,A-Z,0-9]+)/add-items/")
    def add_item_to_order(self, request, order_id=None):
        serializer = ItemListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        items = serializer.data.get("items")
        service_response = OrderSerivce.add_item_to_order(order_id=order_id, items=items)
        return Response(
            data=dict(
                store=OrderSerializer(service_response).data), 
            status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        operation_description="Get all orders",
        operation_summary="Get all orders",
        tags=["Order"],
    )
    def list(self, request, store_id=None):
        service_response = OrderSerivce.list_order()
        return Response(
            data=dict(
                store=OrderSerializer(service_response, many=True).data), 
            status=status.HTTP_200_OK)

    
    @swagger_auto_schema(
        operation_description="Retrieve an order",
        operation_summary="Retrieve an order",
        tags=["Order"],
    )

    def retrieve(self, request, pk=None):
        service_response = OrderSerivce.get_order(id=pk)
        
        return Response(
            data=dict(
                store=OrderSerializer(service_response).data), 
            status=status.HTTP_200_OK)

    
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