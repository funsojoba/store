import uuid
from django.db import models



class BaseAbstractModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        ordering = ('-created_at',)
    
    def save(self, actor=None, *args, **kwargs):
        if not self.pk:
            self.created_by = actor
        super(BaseAbstractModel, self).save(*args, **kwargs)
    