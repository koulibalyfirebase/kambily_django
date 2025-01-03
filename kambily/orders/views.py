from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order, OrderItem, Cart
from accounts.models import CustomUser  # Modifiez selon votre projet
from products.models import Product  # Modifiez selon votre projet
from .serializers import CartSerializer

class OrderView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Récupérer l'utilisateur via son email
        email = request.data.get("email")
        p = request.data.get("product")
        quantity = request.data.get("quantity")
        print(email, p, quantity)
        try:
            user = CustomUser.objects.get(email=email)
            product = Product.objects.get(pk=p)
            
            cart = Cart.objects.create(
                user=user,
                product=product,
                quantity=quantity
            )
            
            return Response(CartSerializer(cart).data, status=200)
        except:
            return Response({'message': 'utilisateur non trouvé'}, status=404)
        
        # Récupérer le panier de l'utilisateur
        # cart_items = Cart.objects.filter(user=user)
        # if not cart_items.exists():
        #     return JsonResponse({'error': 'Votre panier est vide'}, status=400)
        
        # Calculer le prix total
        # total_price = sum(item.product.price * item.quantity for item in cart_items)
        
        # Créer une commande
        # order = Order.objects.create(customer=user, total_price=total_price, status='pending')
        
        # Créer des éléments de commande
        # for item in cart_items:
        #     OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
        
        # Vider le panier
        # cart_items.delete()    
