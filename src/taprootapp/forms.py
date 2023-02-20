from django import forms 
from .models import PantryItem, FridgeItem


class PantryItemForm(forms.ModelForm):
    category = forms.ChoiceField(choices=PantryItem.PANTRY_TYPES)

    class Meta:
        model = PantryItem
        fields = ['category', 'item_name', 'expiry_date', 'quantity']
        widgets = {
            'item_name': forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'Write something'}),
            'category': forms.CheckboxSelectMultiple(),
            'expiry_date': forms.SelectDateWidget(),
        }


class FridgeItemForm(forms.ModelForm):
    category = forms.ChoiceField(choices=FridgeItem.FRIDGE_TYPES)

    class Meta:
        model = FridgeItem
        fields = ['item_name', 'category', 'expiry_date', 'quantity']
        widgets = {
            'item_name': forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'Write something...'}),
            'category': forms.CheckboxSelectMultiple(),
            'expiry_date': forms.SelectDateWidget(),
        }
###
# class FridgeTestForm(forms.ModelForm):
#     class Meta:
#         model = FridgeItem
#         fields = ["item_name", "category", "expiry_date", "quantity"]

# class PantryTestForm(forms.ModelForm):
#     class Meta:
#         model = PantryItem
#         fields = ["item_name", "category", "expiry_date", "quantity"]
###