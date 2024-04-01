from django.shortcuts import render
from .models import Product


def all_products(request):

    products = Product.objects.all()
    category = None
    if 'category' in request.GET:
        category = request.GET['category']
        products = products.filter(category__name=category)
        
    context = {
        "products": products,
    }
    return render (request, 'products/products.html', context)