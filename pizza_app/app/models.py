from django.db import models
from django.core.validators import MaxValueValidator
# pizza choices for dropdowns
# should be moved to be like django 3+ implementation later
size_choice = (
    ('small', 'SMALL'),
    ('medium', 'MEDIUM'),
    ('large', 'LARGE'),
)

crust_choice = (
    ('normal', 'NORMAL'),
    ('thin', 'THIN'),
    ('thick', 'THICK'),
    ('gluten free', 'GLUTEN FREE'),
)

sauce_choice = (
    ('tomato', 'TOMATO'), 
    ('bbq', 'BBQ'),
)

cheese_choice = (
    ('mozzarella', 'MOZZARELLA'),
    ('vegan', 'VEGAN'),
    ('low-fat', 'LOW FAT'),
)

class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.CharField(max_length=6, choices=size_choice, default='medium')
    crust = models.CharField(max_length=11, choices=crust_choice, default='normal')
    sauce = models.CharField(max_length=6, choices=sauce_choice, default='tomato')
    cheese = models.CharField(max_length=10, choices=size_choice, default='mozzarella')
    pepperoni = models.BooleanField(default=False)
    chicken = models.BooleanField(default=False)
    ham = models.BooleanField(default=False)
    pineapple = models.BooleanField(default=False)
    pepper = models.BooleanField(default=False)
    mushroom = models.BooleanField(default=False)
    onion = models.BooleanField(default=False)

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(default='Your Name Here')
    address = models.TextField(default='Your Address Here')
    card = models.IntegerField(default=0)
    expiry = models.CharField(default='MM/YY', max_length=5)
    cvv = models.IntegerField(default=000, validators=[MaxValueValidator(999)])

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)