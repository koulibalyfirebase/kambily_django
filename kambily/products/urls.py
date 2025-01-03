from django.urls import path
from . views import ProductListView

urlpatterns = [
    path('index', view=ProductListView.as_view(), name="index")
]
