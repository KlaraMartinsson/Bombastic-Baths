from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_wishlist, name='view_wishlist'),
    path('wishlist/add/<slug:slug>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<slug:slug>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist/clear/', views.clear_wishlist, name='clear_wishlist'),
]