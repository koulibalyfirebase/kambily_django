from rest_framework import serializers
from orders.models import Cart
from accounts.serializers import CustomerProfile

class CartSerializer(serializers.ModelSerializer):
    user = CustomerProfile()
    
    class Meta:
        model = Cart
        fields = [
            'id', 'user', 'product', 'quantity'
        ]