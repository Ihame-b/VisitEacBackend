from dataclasses import fields
from django import forms

from Papi.models import Product



class CreateProducts(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['productname']