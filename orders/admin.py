from django.contrib import admin
from django.contrib.admin import TabularInline
from .models import Order, OrderItem


class OrderItemAdminInline(TabularInline):
    model = OrderItem
    fields = ("order", "product", "quantity", "quantity_total_price")
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "is_paid", "datetime_created",
                    "datetime_modified")
    inlines = (OrderItemAdminInline, )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity", "quantity_total_price")
