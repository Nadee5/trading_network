from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'model', 'release_date',)
    search_fields = ('title', 'model',)
    ordering = ('release_date',)
