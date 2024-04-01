from django.shortcuts import render, get_object_or_404
import random
from .models import Product, Gift, Category


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
    categories = None
    title = "All Bath Bombs"

    if 'category' in request.GET:
        category = request.GET['category']
        bathbombs = bathbombs.filter(category__name=category)
        category = get_object_or_404(Category, name=category)
        title = category.get_friendly_name()
        
    context = {
        "bathbombs": bathbombs,
        "current_categories": categories,
        "title": title,
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

