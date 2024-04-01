from django.shortcuts import render
from .models import Product, Gift


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

def all_gifts(request):

    gifts = Gift.objects.all()
    category = None
    if 'category' in request.GET:
        category = request.GET['category']
        products = products.filter(category__name=category)
        
    context = {
        "gifts": gifts,
    }
    return render (request, 'products/products.html', context)