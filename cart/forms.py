from django import forms


class CartForm(forms.Form):
    QUANTITY_CHOICES = [(num, str(num))for num in range(1, 21)]
    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int)
    replace = forms.BooleanField(required=False, widget=forms.HiddenInput)
