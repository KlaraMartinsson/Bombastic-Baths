"""Bombastic Baths URL Configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include("checkout.urls")),
    path('profile/', include('profiles.urls')),
    path('wishlist/', include('wishlist.urls')),
]

handler403 = 'home.views.custom_403'
handler404 = 'home.views.custom_404'
handler405 = 'home.views.custom_405'
handler500 = 'home.views.custom_500'