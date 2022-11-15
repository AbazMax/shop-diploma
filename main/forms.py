from django import forms
from .models import UserMessage, Checkout
from cart.cart import Cart

class UserMessage(forms.ModelForm):

    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Name',
            'name': 'name',
            'id': 'name',
        })
    )

    email = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'email',
            'placeholder': 'Email',
            'name': 'email',
            'id': 'email'
        })
    )

    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'type': 'tel',
            'placeholder': 'Phone in format xxx xxx xxxx',
            'name': 'phone',
            'id': 'phone',
            'required pattern': '^(\d{3}[- .]?){2}\d{4}$'
        })
    )

    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Subject',
            'name': 'subject',
            'id': 'subject'
        })
    )

    message = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={
            'name': 'message',
            'id': 'message',
            'cols': '30',
            'rows': '10',
            'placeholder': 'Message'
        })

    )

    class Meta:
        model = UserMessage
        fields = ('name', 'phone', 'email', 'subject', 'message')


class Order(forms.ModelForm):

    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Name',
        })
    )

    email = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'email',
            'placeholder': 'Email',
        })
    )

    address = forms.CharField(
        max_length=500,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'address',
        })
    )

    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'type': 'tel',
            'placeholder': 'Phone in format xxx xxx xxxx',
            'required pattern': '^(\d{3}[- .]?){2}\d{4}$'
        })
    )

    shipping_address = forms.CharField(
        max_length=500,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Shipping address',
        })
    )

    comment = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={
            'name': 'bill',
            'id': 'bill',
            'cols': '30',
            'rows': '10',
            'placeholder': 'Comment'
        })
    )

    class Meta:
        model = Checkout
        fields = ('name', 'email', 'address', 'phone', 'shipping_address', 'comment')