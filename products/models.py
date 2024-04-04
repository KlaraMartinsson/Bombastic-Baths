from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string


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

    
class Occasion(models.Model):
    """
    Model for gifts occasion
    """

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Gift(models.Model):
    """
    Model for gifts
    """
    occasion = models.ForeignKey('Occasion', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    slug = models.SlugField(max_length=300, blank=True, editable=False, unique=True)
    name = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    quantity = models.IntegerField(blank=False) 

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