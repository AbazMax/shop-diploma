from django import forms
from .models import UserMessage
from django.utils.translation import gettext_lazy


class UserMessage(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': gettext_lazy('name'),
            'name': 'name',
            'id': 'name',
        })
    )

    email = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'email',
            'placeholder': gettext_lazy('Email'),
            'name': 'email',
            'id': 'email'
        })
    )

    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'type': 'tel',
            'placeholder': gettext_lazy('Phone in format xxx xxx xxxx'),
            'name': 'phone',
            'id': 'phone',
            'required pattern': '^(\d{3}[- .]?){2}\d{4}$'
        })
    )

    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': gettext_lazy('Subject'),
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
            'placeholder': gettext_lazy('Message')
        })

    )

    class Meta:
        model = UserMessage
        fields = ('name', 'phone', 'email', 'subject', 'message')

