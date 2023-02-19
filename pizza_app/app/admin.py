from django.contrib import admin
from .models import *

admin.site.register(Pizza)
admin.site.register(Order)
admin.site.register(Customer)

admin.site.register(Size)
admin.site.register(Crust)
admin.site.register(Sauce)
admin.site.register(Cheese)