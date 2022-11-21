from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Name'
        })
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'email',
            'placeholder': 'email'
        })
    )

    address = forms.CharField(
        max_length=500,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'billing address',
        })
    )

    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Phone number in format xxx xxx xxxx',
            'data-rule': 'minlen:10',
            'data-msg': 'Phone number in format xxx xxx xxxx',
            'pattern': '^(\d{3}[- .]?){2}\d{4}$'
        })
    )

    shipping_address = forms.CharField(
        max_length=500,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'shipping address',
        })
    )

    comment = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={
            'name': 'bill',
            'id': 'bill',
            'cols': '30',
            'rows': '10',
            'placeholder': 'Comment',
        })
    )

    class Meta:
        model = Order
        fields = ['name', 'email', 'address', 'phone', 'shipping_address', 'comment']
