from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import PizzaForm, CustomerForm
from .models import Order, Customer, Pizza
from django.views.generic import TemplateView

def index(request):
    if request.method == "POST":
        form = PizzaForm(request.POST)
        pizz = form.save()
        # move pizza_id to session so we can use it later in details
        request.session['pizz_id'] = pizz.id
        # dont need validation ass only dropdowns and booleans
        cust_form = CustomerForm()
        return render(request, 'details.html', {'form': cust_form})
    
    else:
        # get
        form = PizzaForm()
        return render(request, 'index.html', {'form': form})

def details(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            cust = form.save()
            
            # get pizza from session in index view
            pizz = request.session.get('pizz_id')
            pizza = Pizza.objects.filter(id=pizz).first()
            
            # extract toppings for nice templating
            toppings = {'pepperoni': pizza.pepperoni, 'chicken': pizza.chicken, 'ham': pizza.ham, 'pineapple': pizza.pineapple, 'pepper': pizza.pepper, 'mushroom': pizza.mushroom, 'onion': pizza.onion}
            
            # make order
            order = Order(customer=cust, pizza=pizza)
            order.save()
            # make dicts of the object so we can print nicer in the template
            # could give order model but nastier template then
            return render(request, 'final.html', {'pizza' : order.pizza.__dict__, 'customer' : order.customer.__dict__, 'toppings' : toppings})
    
        else:
            # bad form
            return render(request, 'details.html', {'form': form})
    
    else:
        # get
        form = CustomerForm()
        return render(request, 'details.html', {'form': form})