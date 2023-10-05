from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("first_name", "last_name", "phone_number", "note", "address")
        widgets = {"address": forms.Textarea(attrs={"rows": 3}),
                   "note": forms.Textarea(attrs={"rows": 2}
                                          )}
