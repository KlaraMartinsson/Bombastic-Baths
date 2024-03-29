from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.our_story, name='ourstory'),
    path('privacypolicy/', views.privacy_policy, name='privacypolicy'),
]