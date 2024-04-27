from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_wishlist, name='view_wishlist'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist/clear/<int:product_id>/', views.clear_wishlist, name='clear_wishlist'),
]