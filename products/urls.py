from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('bathbombs/', views.all_bathbombs, name='bathbombs'),
    path('gifts/', views.all_gifts, name='gifts'),
    path('product_details/', views.product_details, name='details'),
]