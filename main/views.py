from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    info = Info.objects.first()
    partners = Partners.objects.filter(is_visible=True)
    contacts = Contacts.objects.first()
    products = Product.objects.filter(is_visible=True).order_by('?')
    promo = Promo.objects.first()
    testimonials = Testimonials.objects.filter(is_visible=True)
    about = About.objects.first()
    banner = Banner.objects.filter(is_visible=True)


    data = {
        'info': info,
        'partners': partners,
        'contacts': contacts,
        'products': products,
        'promo': promo,
        'testimonials': testimonials,
        'about': about,
        'banner': banner,
            }

    return render(request, 'home.html', context=data)

