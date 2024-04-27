from django.db import models

from django.contrib.auth.models import User
from products.models import Product

class Wishlist(models.Model):
    """A model for a user's wishlist"""
    #Each user can only have one wishlist
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    #A single wishlist can contain multiple products
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"