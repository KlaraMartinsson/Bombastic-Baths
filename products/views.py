from django.db.models import Q
from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models.functions import Lower

from .models import Product, Category, Rating
from wishlist.models import Wishlist


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
    user = request.user

    if user.is_authenticated:
        wishlist, created = Wishlist.objects.get_or_create(user=user)
    else:
        wishlist = None
    
    # Sorting functionality
    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
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
        'wishlist': wishlist,
    }
    return render(request, 'products/products.html', context)

def product_details(request, slug):
    """ A view to show individual bath bomb details """

    products = Product.objects.all()
    product = get_object_or_404(products, slug=slug)
    user = request.user

    if request.user.is_authenticated:
        wishlist, created = Wishlist.objects.get_or_create(user=user)
    else:
        wishlist = None
        
    context = {
        'product': product,
        'wishlist': wishlist,
    }
    return render (request, 'products/product_details.html', context)


