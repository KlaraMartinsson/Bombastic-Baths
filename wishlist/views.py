from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from .models import Wishlist
from profiles.models import UserProfile
from products.models import Product


def view_wishlist(request):
    """ A view to return the wishlist page """
    if not request.user.is_authenticated:
        messages.error(
            request, "Sorry, you need to be logged in to add to your Wishlist."
        )
        return redirect(reverse("account_login"))

    template = "wishlist/wishlist.html"
    context = {
    }

    return render(request, template, context)