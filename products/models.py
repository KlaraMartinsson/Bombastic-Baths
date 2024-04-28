from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.crypto import get_random_string
from django.db.models import Avg, Count


class Category(models.Model):
    """
    Model for product categories
    """
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    """
    Model for products
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    slug = models.SlugField(max_length=300, blank=True, editable=False, unique=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    ingredients = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """
        Creates a random sku, and a slug based on the name and the sku 
        """
        if not self.sku:
            self.sku = get_random_string(6).upper()

        if not self.slug:
            base_slug = slugify(self.name)
            sku = self.sku
            unique_slug = f"{base_slug}-{sku}"
            self.slug = unique_slug

        super().save(*args, **kwargs)

    def average_rating(self):
        reviews = Rating.objects.filter(product=self).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg
    
    def count_rating(self):
        reviews = Rating.objects.filter(product=self).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.user} gave {self.product} a {self.rating} star rating"