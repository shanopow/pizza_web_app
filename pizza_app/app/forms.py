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
        widgets = {
            'expiry': forms.TextInput(attrs={'placeholder': 'MM/YY'}),
        }
    
    
    '''
    def clean(self):
        # extract data
        data = self.cleaned_data
        card = data['card']
        expiry_date = data['expiry']
        cvv = data['cvv']

        try:
            exp_m = int(expiry_date[0:2])
            exp_y = int(expiry_date[3:5])
            if expiry_date[2] != '/':
                raise forms.ValidationError('Invalid Expiry Date')
        except:
            raise forms.ValidationError('Invalid Expiry Date')
        
        if len(cvv) != 3:
            raise forms.ValidationError('Invalid CVV') 

        elif len(card) > 19 or len(card) < 4:
            raise forms.ValidationError('Invalid card Number')
        
        return data
    '''