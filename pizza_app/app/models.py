from django.db import models
from django.utils.translation import gettext_lazy as _

# pizza choices for dropdowns
# move to be like django 3+ implementation with subclasses later
size_choice = (
    ('Small', 'SMALL'),
    ('Medium', 'MEDIUM'),
    ('Large', 'LARGE'),
)

crust_choice = (
    ('Normal', 'NORMAL'),
    ('Thin', 'THIN'),
    ('Thick', 'THICK'),
    ('Gluten free', 'GLUTEN FREE'),
)

sauce_choice = (
    ('Tomato', 'TOMATO'), 
    ('Bbq', 'BBQ'),
)

cheese_choice = (
    ('Mozzarella', 'MOZZARELLA'),
    ('Vegan', 'VEGAN'),
    ('Low-fat', 'LOW FAT'),
)

# models
class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.CharField(max_length=6, choices=size_choice, default='Medium')
    crust = models.CharField(max_length=11, choices=crust_choice, default='Normal')
    sauce = models.CharField(max_length=6, choices=sauce_choice, default='Tomato')
    cheese = models.CharField(max_length=10, choices=size_choice, default='Mozzarella')
    pepperoni = models.BooleanField(default=False)
    chicken = models.BooleanField(default=False)
    ham = models.BooleanField(default=False)
    pineapple = models.BooleanField(default=False)
    pepper = models.BooleanField(default=False)
    mushroom = models.BooleanField(default=False)
    onion = models.BooleanField(default=False)

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default='Your Name Here', max_length=256)
    address = models.CharField(default='Your Address Here', max_length=256)
    card = models.IntegerField(default=0)
    expiry = models.CharField(default='MM/YY', max_length=5)
    cvv = models.IntegerField(default=000)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)