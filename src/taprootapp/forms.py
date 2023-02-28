from django import forms 
from .models import PantryItem, FridgeItem, Recipe, RecipeRestriction
from django.contrib.auth.models import User

class PantryItemForm(forms.ModelForm):
    category = forms.ChoiceField(choices=PantryItem.PANTRY_TYPES)

    class Meta:
        model = PantryItem
        fields = ['category', 'item_name', 'expiry_date', 'quantity']
        widgets = {
            'item_name': forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'Enter item name'}),
            'category': forms.CheckboxSelectMultiple(),
            'expiry_date': forms.SelectDateWidget(attrs={'class':''}),
        }


class FridgeItemForm(forms.ModelForm):
    category = forms.ChoiceField(choices=FridgeItem.FRIDGE_TYPES)

    class Meta:
        model = FridgeItem
        fields = ['category','item_name', 'expiry_date', 'quantity']
        widgets = {
            'item_name': forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'Enter item name'}),
            'category': forms.Select(),
            'quantity': forms.NumberInput(attrs={'placeholder' : 'Enter quantity'}),
            'expiry_date': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")),
        }


class RecipeForm(forms.ModelForm):
    restrictions = forms.MultipleChoiceField(choices=Recipe.DIETARY_RESTRICTIONS, widget=forms.CheckboxSelectMultiple)
    cuisine = forms.MultipleChoiceField(choices=Recipe.CUISINE_TYPES, widget=forms.CheckboxSelectMultiple)
    flavor_profile = forms.MultipleChoiceField(choices=Recipe.FLAVOR_PROFILES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Recipe
        fields = ['title', 'restrictions', 'cuisine', 'flavor_profile', 'ingredients', 'instructions', 'source', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter recipe name'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter ingredients separated by commas'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter instructions'}),
            'source': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'www.example.com'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }