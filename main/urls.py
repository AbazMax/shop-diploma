from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contact', views.contact),
    path('shop', views.shop),
    path('<slug:slug>', views.product_detail, name='product_detail'),
]