from .models import Brand, Bike, Sale
from django.contrib import admin

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Brand, BrandAdmin)

class BikeAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'brand', 'stock', 'available']
    list_editable = ['price', 'stock', 'available']
    list_per_page = 10

admin.site.register(Bike, BikeAdmin)

class SaleAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'original_price', 'sale_price', 'available']
    list_editable = ['available', 'sale_price']
    list_per_page = 10
admin.site.register(Sale, SaleAdmin)