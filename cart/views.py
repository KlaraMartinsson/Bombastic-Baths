from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from products.models import Product

def shopping_cart(request):
    """A view that renders the shopping cart contents page"""
    
    return render (request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """Add a quantity of the specified product to the shopping cart"""
    
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)

def adjust_cart(request, item_id):
    """ Updates cart """
    cart = request.session.get('cart', {})
    bathbomb = get_object_or_404(Product, pk=item_id)
    quantity = request.POST.get('quantity')

    if item_id in list(cart.keys()):
        if int(quantity) > 0:
            cart[item_id] = quantity
            messages.success(
                request, f'{bathbomb.name} quantity updated successfully.')
        else:
            messages.error(request, 'Something went wrong. Please try again.')

    request.session['cart'] = cart

    return redirect(reverse('cart'))