from django import forms
from .models import *


class ProductForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = '__all__'
        exclude = ['username', 'color']
