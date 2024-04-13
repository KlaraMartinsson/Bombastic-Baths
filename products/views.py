from django.db.models import Q
from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.db.models.functions import Lower
import random
from .models import Product, Gift, Category


def all_products(request):
    """ 
    A view to show all products. 
    Also includes sorting and search queries.
    """

    bathbombs = Product.objects.all().order_by('?')
    gifts = Gift.objects.all().order_by('?')
    query = None
    sort = None
    direction = None
    
    # Sorting functionality
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                bathbombs = bathbombs.annotate(lower_name=Lower('name'))
                gifts = gifts.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            bathbombs = bathbombs.order_by(sortkey)
            gifts = gifts.order_by(sortkey)

        # Search functionality
        if "q" in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please, enter search criteria.")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            bathbombs = bathbombs.filter(queries)
            gifts = gifts.filter(queries)
    
    current_sorting = f'{sort}_{direction}'
    
    # Combine products and gifts into a single list
    products = list(bathbombs) + list(gifts)

    context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


def all_bathbombs(request):
    """ A view to show all bath bombs and sort them"""

    bathbombs = Product.objects.all()
    categories = None
    sort = None
    direction = None
    title = "All Bath Bombs"

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                bathbombs = bathbombs.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            bathbombs = bathbombs.order_by(sortkey)

        if 'category' in request.GET:
            category = request.GET['category']
            bathbombs = bathbombs.filter(category__name=category)
            category = get_object_or_404(Category, name=category)
            title = category.get_friendly_name()

    current_sorting = f'{sort}_{direction}'
        
    context = {
        'bathbombs': bathbombs,
        'categories': categories,
        'title': title,
        'current_sorting': current_sorting,
    }
    return render (request, 'products/bathbombs.html', context)


def all_gifts(request):
    """ A view to show all gifts and sort them"""

    gifts = Gift.objects.all()
    category = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                gifts = gifts.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            gifts = gifts.order_by(sortkey)

        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name=category)
    
    current_sorting = f'{sort}_{direction}'
        
    context = {
        'gifts': gifts,
        'current_sorting': current_sorting,
    }
    return render (request, 'products/gifts.html', context)

def bathbombs_details(request, slug):
    """ A view to show individual bath bomb details """

    bathbombs = Product.objects.all()
    product = get_object_or_404(bathbombs, slug=slug)
        
    context = {
        'product': product,
    }
    return render (request, 'products/product_details.html', context)

def gifts_details(request, slug):
    """ A view to show individual gift details """

    gifts = Gift.objects.all()
    product = get_object_or_404(gifts, slug=slug)
        
    context = {
        'product': product,
    }
    return render (request, 'products/product_details.html', context)

