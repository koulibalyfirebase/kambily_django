from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Order, OrderItem, Cart
from accounts.models import CustomUser  # Modifiez selon votre projet

def place_order(request, email):
    # Récupérer l'utilisateur via son email
    user = get_object_or_404(CustomUser, email=email)
    
    # Récupérer le panier de l'utilisateur
    cart_items = Cart.objects.filter(user=user)
    if not cart_items.exists():
        return JsonResponse({'error': 'Votre panier est vide'}, status=400)
    
    # Calculer le prix total
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    # Créer une commande
    order = Order.objects.create(customer=user, total_price=total_price, status='pending')
    
    # Créer des éléments de commande
    for item in cart_items:
        OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
    
    # Vider le panier
    cart_items.delete()
    
    return JsonResponse({'message': 'Commande passée avec succès', 'order_id': order.id})
