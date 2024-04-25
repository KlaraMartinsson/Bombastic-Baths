from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('bathbombs/', views.all_bathbombs, name='bathbombs'),
    path('<slug:slug>/', views.bathbombs_details, name='bathbomb-details'),

]