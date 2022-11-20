from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('shop', views.shop, name='shop'),
    path('<slug:slug>', views.product_detail, name='product_detail'),

]