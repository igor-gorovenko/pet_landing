from django import forms


class CreateOrderForm(forms.Form):
    username = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=40)