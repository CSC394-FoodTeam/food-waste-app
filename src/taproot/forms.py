from django import forms 


from .models import PantryItem, FridgeItem


class PantryItemForm(forms.ModelForm):
    category = forms.ChoiceField(choices=PantryItem.PANTRY_TYPES)

    class Meta:
        model = PantryItem
        fields = ['category']
        widgets = {
            'category': forms.CheckboxSelectMultiple(),
            'item_name': forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'Write something'}),
        }


class FridgeItemForm(forms.ModelForm):
    category = forms.ChoiceField(choices=FridgeItem.FRIDGE_TYPES)

    class Meta:
        model = FridgeItem
        fields = ['category', 'item_name']
        widgets = {
            'category': forms.CheckboxSelectMultiple(),
            'item_name': forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'Write something'}),
        }