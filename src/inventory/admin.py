from django.contrib import admin
from .models import Inventory
from .models import Fridge, Pantry

# Register your models here.
admin.site.register(Inventory)
admin.site.register(Fridge)
admin.site.register(Pantry)