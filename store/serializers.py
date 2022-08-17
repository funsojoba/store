from .models import Store
from rest_framework import serializers
from authentication.serializers import UserSerializer



class StoreSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        fields = ('id', 'name', 'description', 'location', 'owner')
        model =Store