from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<slug:slug>/', views.product_details, name='product-details'),
    path('remove_review/<slug:slug>/<int:review_id>',
        views.remove_review, name='remove-review'),
    path("<slug:slug>/edit_review/<int:review_id>",
         views.edit_review, name="edit-review"),
]
