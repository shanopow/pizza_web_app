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

    def clean(self):
        allowed_months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        data = self.cleaned_data

        dat = data['expiry']
        data_m = dat[0:2]
        
        if len(str(dat)) != 5:
            raise forms.ValidationError('Invalid Expiry Date')
        elif dat[2] != '/':
            raise forms.ValidationError('Invalid Expiry Date')
        
        if data_m not in allowed_months:
            raise forms.ValidationError('Invalid Expiry Date')


        if len(str(data['cvv'])) != 3:
            raise forms.ValidationError('Invalid CVV') 


        if len(str(data['card'])) > 19 or len(str(data['card'])) < 4:
            raise forms.ValidationError('Invalid card Number')
        
        return data


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