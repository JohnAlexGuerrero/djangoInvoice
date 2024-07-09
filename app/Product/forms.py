from django import forms
from django.forms import Form
from Product.models import Product

class ProductNewForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ("description","brand","codebar","stock","unit","cost","price","weigth")
