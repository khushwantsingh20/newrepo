# forms.py
from django import forms


class ProductFilterForm(forms.Form):
    PRODUCT_CHOICES = (
        ('', 'All Products'),
        ('phone', 'Phone'),
        ('laptop', 'Laptop'),
        ('keyboard', 'Keyboard'),
        ('book', 'Book'),
        ('tshirt', 'T-Shirt'),
        ('mouse', 'Mouse'),
        ('shoes', 'Shoes'),
        ('bags', 'Bags'),
        ('toy', 'Toy'),
        ('electonics', 'Electronics'),
        ('kitchen', 'Kitchen'),
    )

    product_type = forms.ChoiceField(choices=PRODUCT_CHOICES, required=False)

# forms.py
# forms.py

from django import forms

class AddressForm(forms.Form):
    address = forms.CharField(max_length=255, required=True)
    # Add other form fields as needed




