from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Product, Info, Contacts, Partners
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    info = Info.objects.first()
    contacts = Contacts.objects.first()
    partners = Partners.objects.filter(is_visible=True)
    data = {
        'info': info,
        'contacts': contacts,
        'partners': partners,
        'cart': cart,
    }

    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial=
                                                          {'quantity': item['quantity'],
                                                           'update': True
                                                           })
    return render(request, 'cart/cart.html', context=data)
