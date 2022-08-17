from rest_framework import serializers


from .models import Order, Item


from store.serializers import StoreSerializer
from authentication.serializers import UserSerializer


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Item


class OrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=True)
    customer = UserSerializer(read_only=True)
    
    class Meta:
        fields = '__all__'
        model = Order
        
class CreateOrderSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    store_id = serializers.CharField()
    items = serializers.JSONField(default=list)
    state = serializers.ChoiceField(choices=Order.ORDER_STATE)
    

class ItemListSerializer(serializers.Serializer):
    items = serializers.ListField(child=serializers.CharField())