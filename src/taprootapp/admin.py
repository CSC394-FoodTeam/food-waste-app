from django.contrib.auth.admin import admin, UserAdmin
from .models import User, PantryItem, FridgeItem, Recipe
from .forms import PantryItemForm, FridgeItemForm, RecipeForm

admin.site.register(User, UserAdmin)

admin.site.register(PantryItem)
class PantryItemAdmin(admin.ModelAdmin):
    form = PantryItemForm

admin.site.register(FridgeItem)
class FridgeItemAdmin(admin.ModelAdmin):
    form = FridgeItemForm

admin.site.register(Recipe)
class RecipeFormAdim(admin.ModelAdmin):
    form = RecipeForm