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
    """Changes the quantity of products to the specified amount"""
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


def remove_from_cart(request, item_id):
    """Removes items from shopping cart"""

    cart = request.session.get('cart', {})
    bathbomb = get_object_or_404(Product, pk=item_id)
    if item_id in cart.keys():
        try:
            cart.pop(item_id)
            messages.success(request, f'{bathbomb.name} removed from cart.')
            request.session['cart'] = cart
            return redirect(reverse('cart'))
        except Exception as e:
            messages.error(request, f'An error occured {e}')
            return redirect(reverse('cart'))
   