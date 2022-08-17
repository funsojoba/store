from django.db import models

from helpers.db_helpers.base_model import BaseAbstractModel

from store.models import Store





class Item(BaseAbstractModel):
    
    ITEM_STATUS = (
        ('AVAILABLE', 'AVAILABLE'),
        ('OUT_OF_STOCK', 'OUT_OF_STOCK'),
    )
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(max_length=50, choices=ITEM_STATUS, default='AVAILABLE')

    def __str__(self):
        return self.name


class Order(BaseAbstractModel):
    ORDER_STATE = (
        ('OPEN', 'OPEN'),
        ('CANCELED', 'CANCELED'),
        ('DELIVERED', 'DELIVERED'),
    )
    name =models.CharField(max_length=100)
    description =models.TextField()
    store = models.ForeignKey("store.Store", on_delete=models.CASCADE, related_name="order")
    state = models.CharField(max_length=10, choices=ORDER_STATE, default='OPEN')
    item = models.ManyToManyField(to=Item, related_name='order_item', blank=True)
    customer = models.ForeignKey("authentication.User", 
                                 on_delete=models.CASCADE, 
                                 related_name="order_owner", 
                                 null=True, blank=True)
    
    
    def __str__(self):
        return self.name
        
