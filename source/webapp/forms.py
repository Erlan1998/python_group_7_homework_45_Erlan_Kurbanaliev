from django import forms
from webapp.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'quantity', 'price']

class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти')
