from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product',]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'address', 'phone', 'shipping_address',
                    'comment', 'created', 'updated', 'checked']
    list_filter = ['checked', 'created', 'updated']

    inlines = [OrderItemInLine,]


admin.site.register(Order, OrderAdmin,)