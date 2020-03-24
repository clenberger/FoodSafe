from django.forms import ModelForm
from food.models import FoodItem
from django import forms

class FoodForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['item_name', 'description', 'date_expires']