from django.contrib import admin
from .models import User, Recipes, PantryItem, FridgeItem

admin.site.register(User)
admin.site.register(FridgeItem)
admin.site.register(PantryItem)
admin.site.register(Recipes)