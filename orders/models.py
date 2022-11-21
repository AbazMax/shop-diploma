from django.db import models
from main.models import Product
from django.core.validators import RegexValidator


class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=500)
    phone_re = RegexValidator(regex=r'^(\d{3}[- .]?){2}\d{4}$',
                              message='Please enter phone number in format +xxx xx xxx xx xx')
    phone = models.CharField(max_length=15, validators=[phone_re])
    shipping_address = models.CharField(max_length=500)
    comment = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    checked = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'{self.id}. Date - {self.created}. {self.name}. {self.checked}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity

