from django.db import models
from django.contrib.auth.admin import admin, UserAdmin
from django.forms import CheckboxSelectMultiple
from .models import User, PantryItem, FridgeItem, Recipe
from .forms import PantryItemForm, FridgeItemForm, RecipeForm


class PantryItemAdmin(admin.ModelAdmin):
    form = PantryItemForm

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

class FridgeItemAdmin(admin.ModelAdmin):
    form = FridgeItemForm

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

class RecipeFormAdmin(admin.ModelAdmin):
    form = RecipeForm
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        formfield = super().formfield_for_manytomany(db_field, request, **kwargs)
        if db_field.name not in ('restrictions', 'cuisine', 'flavor_profile'):
            return formfield
        formfield.widget = CheckboxSelectMultiple()
        return formfield

admin.site.register(User, UserAdmin)
admin.site.register(PantryItem, PantryItemAdmin)
admin.site.register(FridgeItem, FridgeItemAdmin)
admin.site.register(Recipe, RecipeFormAdmin)