from django.urls import path
from .views import CustomUserViewSet
from .views import LoginView
from .views import RegisterView
from .views import Home

user_list = CustomUserViewSet.as_view({
    'get': 'list',
})

user_detail = CustomUserViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path('index/', user_list, name='user-list'),
    path('show/<int:pk>/', user_detail, name='user-detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='login'),
    path('home/', Home.as_view()),
]
