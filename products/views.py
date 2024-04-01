from django.shortcuts import render
import random
from .models import Product, Gift


def all_products(request):
    products = list(Product.objects.all().order_by('?'))
    gifts = list(Gift.objects.all().order_by('?'))

    # Combine products and gifts into a single list
    items = products + gifts

    # Shuffle the combined list to randomize the order
    random.shuffle(items)

    context = {
        "items": items,
    }
    return render(request, 'products/products.html', context)


def all_bathbombs(request):

    bathbombs = Product.objects.all()
    category = None

    if 'category' in request.GET:
        category = request.GET['category']
        bathbombs = bathbombs.filter(category__name=category)
        
    context = {
        "bathbombs": bathbombs,
    }
    return render (request, 'products/bathbombs.html', context)


def all_gifts(request):

    gifts = Gift.objects.all()
    category = None
    
    if 'category' in request.GET:
        category = request.GET['category']
        products = products.filter(category__name=category)
        
    context = {
        "gifts": gifts,
    }
    return render (request, 'products/gifts.html', context)

