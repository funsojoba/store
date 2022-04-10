from django.contrib.auth.models import User
from helpers.db_helpers.base_model import BaseAbstractModel
from django.db import models


class Category(BaseAbstractModel):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    

class Product(BaseAbstractModel):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/", blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    author  = models.CharField(max_length=255, default="Admin" )
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.name
    
    