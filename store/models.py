from django.db import models

from helpers.db_helpers.base_model import BaseAbstractModel


class Store(BaseAbstractModel):
    name =models.CharField(max_length=100)
    description =models.TextField()
    owner =models.ForeignKey("authentication.User", on_delete=models.CASCADE, related_name="store")
    location =models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name
        
