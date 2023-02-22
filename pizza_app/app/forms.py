from django import forms
from .models import *

# use this for printing holder of model in form choices
class CustomMCF(forms.ModelChoiceField):
    def label_from_instance(self, member):
        return "%s" % member.holder

class PizzaForm(forms.ModelForm):

    size = CustomMCF(queryset=Size.objects.all(), widget=forms.RadioSelect)
    crust = CustomMCF(queryset=Crust.objects.all(), widget=forms.RadioSelect)
    sauce = CustomMCF(queryset=Sauce.objects.all(), widget=forms.RadioSelect)
    cheese = CustomMCF(queryset=Cheese.objects.all(), widget=forms.RadioSelect)
    
    class Meta:
        model = Pizza
        fields = ['size', 'crust', 'sauce', 'cheese', 'pepperoni', 'chicken', 'ham', 'pineapple', 'pepper', 'mushroom', 'onion']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'card', 'expiry', 'cvv']
        errors=[]
        # placeholders for fields
        widgets = {
            'expiry': forms.TextInput(attrs={'placeholder': 'MM/YY'}),
            'cvv': forms.TextInput(attrs={'placeholder': '000'}),
        }

    def clean(self):
        allowed_months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        data = self.cleaned_data

        dat = data['expiry']
        data_m = dat[0:2]
        data_y = dat[3:]
        
        # too short, cant be too long as form is char limited to 5
        if len(str(dat)) != 5:
            errors.append('Expiry Date is too short')
        
        # expiry
        if dat[2] != '/':
            errors.append('Missing "/" between month and year of expiry')
        
        # expiry
        if data_m not in allowed_months:
            errors.append('Month is invalid')
        
        # expiry
        if len(str(data['cvv'])) != 3:
            errors.append('Invalid CVV') 

        # expiry, nasty way, change
        try:
            # make sure give an int
            data_y = int(data_y)
        except:
            errors.append('Year is invalid')
        
        # card length is not weird
        elif len(str(data['card'])) > 19 or len(str(data['card'])) < 4:
            errors.append('Invalid Card Number')
        
        if errors;
            # raise an error if encountered any before in cleaning
            raise ValidationError(errors)
        
        return data