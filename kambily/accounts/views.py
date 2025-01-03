from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, 'accounts/index.html')

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import CustomUser, CustomerProfile, DelivererProfile
from .serializers import CustomUserSerializer, CustomerProfileSerializer, DelivererProfileSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        print(username, password)
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        return Response({"error": "Invalid credentials"}, status=400)
    
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        firstName = request.data.get("firstName")
        lastName = request.data.get("lastName")
        role = request.data.get("role", 'customer')  # Default role is 'customer'
        
        print(username, password, firstName, lastName)
        
         # Check if the username already exists
        if CustomUser.objects.filter(email=username).exists():
            return Response({"error": "Email already exists."}, status=404)
        
        # Hash the password
        hashed_password = make_password(password)
        
                # Create new user
        user = CustomUser(
            first_name=firstName,
            last_name=lastName,
            email=username,
            password=hashed_password,
            role=role,
        )
        user.save()

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        
        # You can authenticate the user right away
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

class CustomUserViewSet(ViewSet):
    
    def list(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            user = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response({"message": "Utilisateur non trouvé" })
        
        # Utilisation du bon serializer basé sur le rôle
        if user.role == 'customer':
            profile = CustomerProfile.objects.get(user=user)
            serializer = CustomerProfileSerializer(profile)
        elif user.role == 'deliverer':
            profile = DelivererProfile.objects.get(user=user)
            serializer = DelivererProfileSerializer(profile)
        else:  # Pour les administrateurs ou autres rôles
            serializer = CustomUserSerializer(user)

        return Response(serializer.data)
