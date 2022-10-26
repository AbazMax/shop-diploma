from modeltranslation.translator import register, TranslationOptions

from .models import Category, Product, Promo, Testimonials, About, WhyUs, Info, Contacts

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'unit')


@register(Promo)
class PromoTranslationOptions(TranslationOptions):
    fields = ('type', 'promo_product', 'title', 'description')


@register(Testimonials)
class TestimonialsTranslationOptions(TranslationOptions):
    fields = ('name', 'profession', 'review')


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title_line_1', 'title_line_2', 'paragraph_1', 'paragraph_2')


@register(WhyUs)
class WhyUsTranslationOptions(TranslationOptions):
    fields = ('delivery_title', 'delivery_text', 'price_title', 'price_text', 'service_title', 'service_text', 'refund_title', 'refund_text')


@register(Info)
class InfoTranslationOptions(TranslationOptions):
    fields = ('main_title_line_1', 'main_title_line_2', 'about_title_line_1', 'about_title_line_2', 'contact_title_line_1', 'contact_title_line_2', 'shop_title_line_1', 'shop_title_line_2', 'our_team_title', 'related_prod_title')


@register(Contacts)
class ContactsTranslationOptions(TranslationOptions):
    fields = ('text', 'address', 'open_hours', 'contact', 'about_short', 'subscribe_text')
