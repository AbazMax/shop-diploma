from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contact', views.contact),
    path('shop', views.shop),
    path('<slug:slug>', views.single_product, name='single_product'),
]