from django import forms
from .models import *

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['size','crust','sauce', 'cheese', 'pepperoni', 'chicken', 'ham', 'pineapple', 'pepper', 'mushroom', 'onion']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'card', 'expiry', 'cvv']