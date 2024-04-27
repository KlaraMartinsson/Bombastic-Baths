from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render

from .models import Wishlist
from products.models import Product



def view_wishlist(request):
    """ A view to return the wishlist page """
    if not request.user.is_authenticated:
        messages.error(
            request, "Sorry, you need to be logged in to add to your Wishlist."
        )
        return redirect(reverse("account_login"))

    # Retrieve or create the user's wishlist
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    context = {
        'wishlist': wishlist,
    }

    return render(request, "wishlist/wishlist.html", context)

@login_required
def add_to_wishlist(request, product_id):
    """ A view to add products to users wishlist page """
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    messages.success(request, f"{product.name} added to your wishlist")
    wishlist.save()
    return redirect('view_wishlist')

@login_required
def remove_from_wishlist(request, product_id):
    """ A view to remove products from users wishlist page """
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.remove(product)
    messages.success(request, f"{product.name} removed from your wishlist")
    wishlist.save()
    return redirect('view_wishlist')

@login_required
def clear_wishlist(request, product_id):
    """ A view to clear all products from users wishlist page """
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.clear()
    messages.success(request, "Your wishlist has been cleared")
    return redirect('view_wishlist')