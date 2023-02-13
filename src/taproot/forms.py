from django import forms 


from .models import PantryItem, FridgeItem


class PantryItemForm(forms.ModelForm):
    category = forms.ChoiceField(choices=PantryItem.PANTRY_TYPES)

    class Meta:
        model = PantryItem
        fields = ["user",'category', 'item_name', "expiry_date", "quantity"]
        widgets = {
            'category': forms.CheckboxSelectMultiple(),
            'item_name': forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'Write something'}),
        }


class FridgeItemForm(forms.ModelForm):
    category = forms.ChoiceField(choices=FridgeItem.FRIDGE_TYPES)

    class Meta:
        model = FridgeItem
        fields = ["user",'category', 'item_name', "expiry_date", "quantity"]
        widgets = {
            'category': forms.CheckboxSelectMultiple(),
            'item_name': forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'Write something'}),
        }
###
class FridgeTestForm(forms.ModelForm):
    class Meta:
        model = FridgeItem
        fields = ["user", "item_name", "category", "expiry_date", "quantity"]

class PantryTestForm(forms.ModelForm):
    class Meta:
        model = PantryItem
        fields = ["user", "item_name", "category", "expiry_date", "quantity"]
###