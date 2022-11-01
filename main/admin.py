from django.contrib import admin
from .models import Category, Promo, Product, Testimonials, About, WhyUs, Partners, Banner, Info, Contacts, UserMessage
from modeltranslation.admin import TranslationAdmin
# Register your models here.

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    pass


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_filter = ('category',)
    list_display = ('name', 'price', 'category', 'position', 'is_visible')
    prepopulated_fields = {'slug': ('name',), }


@admin.register(Promo)
class PromoAdmin(TranslationAdmin):
    list_filter = ('type', 'position',)
    list_display = ('promo_product', 'type', 'end_of_promo', 'is_visible',)


@admin.register(Testimonials)
class TestimonialsAdmin(TranslationAdmin):
    list_display = ('position', 'name', 'is_visible')


@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ('title_line_1', 'title_line_2')


@admin.register(WhyUs)
class WhyUsAdmin(TranslationAdmin):
    list_display = ('delivery_title', 'price_title', 'service_title', 'refund_title')


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible')


@admin.register(Info)
class InfoAdmin(TranslationAdmin):
    pass


@admin.register(Contacts)
class ContactsAdmin(TranslationAdmin):
    pass

@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    pass