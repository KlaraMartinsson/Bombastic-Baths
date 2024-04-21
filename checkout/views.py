from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
      cart = request.session.get('cart', {})
      if not cart:
            messages.error(request, "There's nothing in your cart at the moment")
            return redirect(reverse('products'))

      order_form = OrderForm()
      context = {
            'order_form': order_form,
            'stripe_public_key': 'pk_test_51P7HpS2L3AP7n4WsVj5q8Hrpyn4YYQQoBJ9QNe6elmGjXz0l6PUtAQ3n8LorZtm9S88PdTZ7shOjpuP57zk4IvTO00mTr6NNnZ',
            'client_secret': 'test client secret',
      }

      return render(request, 'checkout/checkout.html', context)