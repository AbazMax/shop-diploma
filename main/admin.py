from django.contrib import admin

# Register your models here.
from .models import Category, Promo, Product, Testimonials, About, WhyUs, Partners, Banner, Info, Contacts


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


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('position', 'name', 'is_visible')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title_line_1', 'title_line_2')


@admin.register(WhyUs)
class WhyUsAdmin(admin.ModelAdmin):
    list_display = ('delivery_title', 'price_title', 'service_title', 'refund_title')


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible')


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    pass


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    pass