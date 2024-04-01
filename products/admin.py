from django.contrib import admin
from .models import Product, Category, Occasion, Gift

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'category', 'name', 'price','image')
    search_fields = ['name']

class ProductCategory(admin.ModelAdmin):
    list_display = ('name', 'friendly_name')
    search_fields = ['name', 'friendly_name']

class GiftAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'price','quantity')
    search_fields = ['name']

class OccasionCategory(admin.ModelAdmin):
    list_display = ('name', 'friendly_name')
    search_fields = ['name', 'friendly_name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, ProductCategory)
admin.site.register(Gift, GiftAdmin)
admin.site.register(Occasion, OccasionCategory)
