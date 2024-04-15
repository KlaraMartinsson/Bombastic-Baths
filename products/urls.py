from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('bathbombs/', views.all_bathbombs, name='bathbombs'),
    path('gifts/', views.all_gifts, name='gifts'),
    path('productinfo/<slug:slug>/', views.bathbombs_details, name='bathbomb-details'),
    path('giftinfo/<slug:slug>/', views.gifts_details, name='gift-details'),
]