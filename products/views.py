from django.db.models import Q
from django.shortcuts import render, redirect,  get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models.functions import Lower

from .forms import RatingForm, ReviewForm

from .models import Product, Category, Rating, Review
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
    product_reviews = product.product_reviews.all().order_by('-created_on')
    user = request.user

    if request.user.is_authenticated:
        wishlist, created = Wishlist.objects.get_or_create(user=user)
        user_rating = Rating.objects.filter(user=request.user, product=product).exists()
    else:
        wishlist = None
        user_rating = False

    if request.method == "POST":
        if 'rating_form' in request.POST:
            rating_form = RatingForm(data=request.POST)
            if rating_form.is_valid() and request.user.is_authenticated:
                rating = rating_form.save(commit=False)
                rating.user = request.user
                rating.product = product
                rating.save()
                messages.success(request,"Product rating submitted.")
                return HttpResponseRedirect(reverse('product-details', args=[slug]))
            else:
                messages.error(request, "Error rating product. Please try again.")
        
        if 'review_form' in request.POST:
            review_form = ReviewForm(data=request.POST)
            if review_form.is_valid() and request.user.is_authenticated:
                review = review_form.save(commit=False)
                review.author = request.user
                review.product = product
                review.save()
                messages.success(request, "Review submitted and awaiting approval.")
                return HttpResponseRedirect(reverse('product-details', args=[slug]))
            else:
                messages.error(request, "Error submitting review")
    
    rating_form = RatingForm()
    review_form = ReviewForm()
        
    context = {
        'product': product,
        'wishlist': wishlist,
        'rating_form': rating_form,
        'user_rating': user_rating,
        'review_form': review_form,
        'product_reviews': product_reviews,
    }
    return render (request, 'products/product_details.html', context)

@login_required
def remove_review(request, slug, review_id):
    """ A view to remove product reviews """

    review = get_object_or_404(Review, pk=review_id)

    if request.user == review.author:
        review.delete()
        messages.success(request, "Review removed.")
    else:
        messages.error(request, "You are not the author of this review.")
    
    return HttpResponseRedirect(reverse('product-details', args=[slug]))

@login_required
def edit_review(request, slug, review_id):
    """ A view to edit product reviews """
    
    if request.method == "POST":
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.product = product
            review.approved = False
            review.save()
            messages.success(request, "Product review edited and awaiting approval")
        else:
            messages.error(request, "Error editing product review")

    return HttpResponseRedirect(reverse('product-details', args=[slug]))

