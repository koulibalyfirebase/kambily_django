from django.urls import path
from . import views

urlpatterns = [
    path('place_order', view=views.OrderView.as_view(), name="place_order")
]
