from rest_framework import serializers
from .models import Product, Category, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  
        
class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['id', 'image'] 
        
    def get_image(self, obj):
        request = self.context.get('request')  # Récupérer la requête pour construire une URL absolue
        if request is not None:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url 
        
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = ProductImageSerializer(many=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'description', 'price', 'images']
