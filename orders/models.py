from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

import movies.models


class Order(models.Model):
    user = models.ForeignKey(verbose_name=_("user"), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name=_("firstname"), max_length=100)
    last_name = models.CharField(verbose_name=_("lastname"), max_length=100)
    is_paid = models.BooleanField(verbose_name=_("is_paid"), default=False)
    address = models.CharField(verbose_name=_("address"), max_length=300)
    phone_number = models.CharField(verbose_name=_("Phone Number"), max_length=15)
    note = models.CharField(verbose_name=_("Order Note"), max_length=700,)
    zarinpal_authority = models.CharField(verbose_name=_("zarinpal authority"), max_length=255, blank=True)
    zarinpal_ref_id = models.CharField(verbose_name=_("ref id"), max_length=150, blank=True)
    zarinpal_data = models.TextField(verbose_name=_("zarinpal data"), blank=True)
    datetime_created = models.DateTimeField(verbose_name=_("datetime_created"), auto_now_add=True)
    datetime_modified = models.DateTimeField(verbose_name=_("datetime_modified"), auto_now=True)

    def get_toman_total_price(self):
        return sum(item.quantity_total_price for item in self.item.all())


class OrderItem(models.Model):
    order = models.ForeignKey(verbose_name=_("order"), to=Order, on_delete=models.CASCADE, related_name="item")
    product = models.ForeignKey(verbose_name=_("product"), to=movies.models.Movie, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name=_("quantity"))
    quantity_total_price = models.PositiveIntegerField(verbose_name=_("total_quantity_price"))

