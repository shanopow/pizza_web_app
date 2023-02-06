from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import PizzaForm, CustomerForm
from .models import Order, Customer, Pizza

def index(request):
    if request.method == "POST":
        form = PizzaForm(request.POST)
        cust_form = CustomerForm(request.POST)
        if form.is_valid():
            pizz = form.save()
            request.session['pizz_id'] = pizz.id
            return render(request, 'details.html', {'form': cust_form, 'pizza':pizz})
        else:
            return render(request, 'index.html', {'form': form})
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
            order = Order(customer=cust, pizza=pizza)
            order.save()
            return render(request, 'final.html', {'order' : order})
        else:
            return render(request, 'details.html', {'form': form})
    else:
        form = CustomerForm()
        return render(request, 'details.html', {'form': form})