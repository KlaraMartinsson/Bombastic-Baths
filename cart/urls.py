from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_cart, name='cart'),
    path('add/<product_id>/', views.add_to_cart, name='add_to_cart'),
]