from django.db import models
from django.utils.translation import gettext_lazy as _

class Size(models.Model):
    id = models.AutoField(primary_key=True)
    holder = models.CharField(max_length = 100, default="TOPPING_NAME_HERE")

class Crust(models.Model):
    id = models.AutoField(primary_key=True)
    holder = models.CharField(max_length = 100, default="TOPPING_NAME_HERE")

class Sauce(models.Model):
    id = models.AutoField(primary_key=True)
    holder = models.CharField(max_length = 100, default="TOPPING_NAME_HERE")

class Cheese(models.Model):
    id = models.AutoField(primary_key=True)
    holder = models.CharField(max_length = 100, default="TOPPING_NAME_HERE")

# models
class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    crust = models.ForeignKey(Crust, on_delete=models.CASCADE)
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    
    pepperoni = models.BooleanField(default=False)
    chicken = models.BooleanField(default=False)
    ham = models.BooleanField(default=False)
    pineapple = models.BooleanField(default=False)
    pepper = models.BooleanField(default=False)
    mushroom = models.BooleanField(default=False)
    onion = models.BooleanField(default=False)

    def size_names(self):
        return [s for s in self.size.all()]

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    card = models.IntegerField()
    expiry = models.CharField(max_length=5)
    cvv = models.IntegerField()

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)