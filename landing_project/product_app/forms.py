from django import forms
from .models import Product

class CreateOrderForm(forms.Form):
    username = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=40)

