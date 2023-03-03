from django import forms 
from .models import PantryItem, FridgeItem, Recipe
# from django.contrib.auth.models import User

class PantryItemForm(forms.ModelForm):
    class Meta:
        model = PantryItem
        fields = ['category', 'item_name', 'expiry_date', 'quantity']
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter item name'}),
            'category': forms.Select(attrs={'class': 'form-control',}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Enter quantity'}),
            'expiry_date': forms.SelectDateWidget(attrs={'class': 'form-control', 'placeholder': "Choose Year", 'placeholder': "Choose Month", 'placeholder': "Choose Day"}),
        }


class FridgeItemForm(forms.ModelForm):
    class Meta:
        model = FridgeItem
        fields = ['category','item_name', 'expiry_date', 'quantity']
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter item name'}),
            'category': forms.Select(attrs={'class': 'form-control',}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Enter quantity'}),
            'expiry_date': forms.SelectDateWidget(attrs={'class': 'form-control', 'placeholder': "Choose Year", 'placeholder': "Choose Month", 'placeholder': "Choose Day"}),
        }


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'restrictions', 'cuisine', 'ingredients', 'instructions', 'source', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter recipe name'}),
            'restrictions': forms.Select(attrs={'class': 'form-control'}),
            'cuisine': forms.Select(attrs={'class': 'form-control'}),
            # 'flavor_profile': forms.SelectMultiple(),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter ingredients separated by commas'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter instructions'}),
            'source': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'www.example.com'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }