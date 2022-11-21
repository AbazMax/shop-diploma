from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from main.models import Info, Contacts, Partners


def order_create(request):

    cart = Cart(request)
    info = Info.objects.first()
    contacts = Contacts.objects.first()
    partners = Partners.objects.filter(is_visible=True)
    order = Order.objects.all()
    data = {
        'info': info,
        'contacts': contacts,
        'partners': partners,
        'order': order,
    }

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            cart.clear()
            return render(request, 'orders/order/created.html', context=data)

    else:
        form = OrderCreateForm()
        info = Info.objects.first()
        contacts = Contacts.objects.first()
        partners = Partners.objects.filter(is_visible=True)
        data = {
            'cart': cart,
            'form': form,
            'info': info,
            'contacts': contacts,
            'partners': partners,
        }
    return render(request, 'orders/order/create.html', context=data)
