from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import PizzaForm, CustomerForm
from .models import Order, Customer, Pizza
from django.views.generic import TemplateView

def index(request):
    if request.method == "POST":
        form = PizzaForm(request.POST)
        pizz = form.save()
        request.session['pizz_id'] = pizz.id
        cust_form = CustomerForm()
        return render(request, 'details.html', {'form': cust_form})
    else:
        form = PizzaForm()
        return render(request, 'index.html', {'form': form})

def details(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            cust = form.save()
            pizz = request.session.get('pizz_id')
            pizza = Pizza.objects.filter(id=pizz).first()
            toppings = {'Pepperoni': pizza.pepperoni, 'Chicken': pizza.chicken, 'Ham': pizza.ham, 'Pineapple': pizza.pineapple, 'Pepper': pizza.pepper, 'Mushroom': pizza.mushroom, 'Onion': pizza.onion}
            order = Order(customer=cust, pizza=pizza)
            order.save()
            dets = cust.__dict__
            print(dets)
            return render(request, 'final.html', {'order' : order, 'toppings': toppings, 'dets': dets})
        else:
            return render(request, 'details.html', {'form': form})
    else:
        form = CustomerForm()
        return render(request, 'details.html', {'form': form})