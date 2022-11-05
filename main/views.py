from django.shortcuts import render, redirect
from .models import *
from .forms import UserMessage
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

    return render(request, 'main/home.html', context=data)


def single_product(request,slug):
    product = Product.objects.get(slug=slug)
    info = Info.objects.first()
    rel_products = Product.objects.filter(is_visible=True).order_by('?')

    data = {
        'product': product,
        'info': info,
        'rel_products': rel_products,
    }

    return render(request, 'main/single-product.html', context=data)


def about(request):
    info = Info.objects.first()
    partners = Partners.objects.filter(is_visible=True)
    contacts = Contacts.objects.first()
    testimonials = Testimonials.objects.filter(is_visible=True)
    about = About.objects.first()
    banner = Banner.objects.filter(is_visible=True)
    whyus = WhyUs.objects.first()

    data = {
        'info': info,
        'partners': partners,
        'contacts': contacts,
        'testimonials': testimonials,
        'about': about,
        'banner': banner,
        'whyus': whyus
            }

    return render(request, 'main/about.html', context=data)

def contact(request):
    if request.method == 'POST':
        message = UserMessage(request.POST)
        if message.is_valid():
            message.save()
            return redirect('/contact')

    info = Info.objects.first()
    partners = Partners.objects.filter(is_visible=True)
    contacts = Contacts.objects.first()
    message = UserMessage()

    data = {
        'info': info,
        'partners': partners,
        'contacts': contacts,
        'message': message
    }

    return render(request, 'main/contact.html', context=data)


def shop(request):
    info = Info.objects.first()
    partners = Partners.objects.filter(is_visible=True)
    contacts = Contacts.objects.first()
    categories = Category.objects.filter(is_visible=True)
    products = Product.objects.filter(is_visible=True)


    data = {
        'info': info,
        'partners': partners,
        'contacts': contacts,
        'categories': categories,
        'products': products,
    }

    return render(request, 'main/shop.html', context=data)

