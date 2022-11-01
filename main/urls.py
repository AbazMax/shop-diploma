from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contact', views.contact),
    path('shop', views.shop),
    path('ok', views.ok),
    path('error', views.error),
]