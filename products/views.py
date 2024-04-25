from django.db.models import Q
from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.db.models.functions import Lower
import random
from .models import Product, Category


def all_products(request):
    """ 
    A view to show all products. 
    Also includes sorting and search queries.
    """

    products = Product.objects.all().order_by('?')
    query = None
    sort = None
    direction = None
    categories = None
    
    # Sorting functionality
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split()
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Search functionality
        if "q" in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please, enter search criteria.")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
    
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
        'current_categories': categories,
    }
    return render(request, 'products/products.html', context)

def product_details(request, slug):
    """ A view to show individual bath bomb details """

    products = Product.objects.all()
    product = get_object_or_404(products, slug=slug)
        
    context = {
        'product': product,
    }
    return render (request, 'products/product_details.html', context)


