from django.contrib import admin
from webapp.models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category',  'price']
    list_filter = ['category']
    search_fields = ['category']
    fields = ['id', 'name', 'category', 'price', 'balance']
    readonly_fields = ['id']

admin.site.register(Product, ProductAdmin)