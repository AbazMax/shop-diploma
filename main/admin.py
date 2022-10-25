from django.contrib import admin

# Register your models here.
from .models import Category, Promo, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    list_display = ('name', 'price', 'category', 'position', 'is_visible')
    prepopulated_fields = {'slug': ('name',), }


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_filter = ('type', 'position',)
    list_display = ('promo_product', 'type', 'end_of_promo', 'is_visible',)

