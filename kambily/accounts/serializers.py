from rest_framework import serializers
from .models import CustomUser, CustomerProfile, DelivererProfile

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'first_name', 'last_name', 'email', 'role',
            'phone_number', 'address', 'is_active', 'is_staff'
        ]

class CustomerProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()  # Sérialisation imbriquée pour l'utilisateur
    favorite_products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = CustomerProfile
        fields = ['id', 'user', 'favorite_products']

class DelivererProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()  # Sérialisation imbriquée pour l'utilisateur
    active_mission = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = DelivererProfile
        fields = ['id', 'user', 'vehicle_type', 'active_mission']
