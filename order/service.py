from django.db import transaction

from .models import Item, Order

from store.models import Store
from store.service import StoreService


class ItemSerivce:
    @classmethod
    def get_item(cls, **kwargs):
        return Item.objects.filter(**kwargs).first()
    
    @classmethod
    def get_all_items(cls):
        return Item.objects.all()


class OrderSerivce:
    
    @classmethod
    def get_order(cls, **kwargs):
        return Order.objects.filter(**kwargs).first()
    
    @classmethod
    def list_order(cls, **kwargs):
        return Order.objects.filter(**kwargs)
    
    @classmethod
    def list_store_order(cls, **kwargs):
        return Order.objects.filter(store__id=kwargs.get("store_id"))
    
    @classmethod
    def create_order(cls, request, **kwargs):
        store = StoreService.get_store(id=kwargs.get("store_id"))
        items = kwargs.get("items")
        
        order = Order.objects.create(
            name=kwargs.get("name"),
            description=kwargs.get("description"),
            store=store, 
            customer=request.user,
            )
        
        with transaction.atomic():
            for element in items:
                item =  ItemSerivce.get_item(id=element)
                order.item.add(item)
                
        return order
    
    @classmethod
    def add_item_to_order(cls, order_id, items):
        order = cls.get_order(id=order_id)
        with transaction.atomic():
            for element in items:
                item =  ItemSerivce.get_item(id=element)
                order.item.add(item)
        return order