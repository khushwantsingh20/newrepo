# forms.py

from django import forms

from cart.models import CartItem

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
    class Meta:
        model = CartItem
        fields = ('quantity')