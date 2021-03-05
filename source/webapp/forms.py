from django import forms
from django.forms import widgets
from webapp.models import category_choices


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label='Продукт')
    description = forms.CharField(max_length=2000, widget=widgets.Textarea, required=False,label='Информация')
    category = forms.ChoiceField(choices=category_choices, label='Категория')
    quantity = forms.IntegerField(label='Кол', min_value=0)
    price = forms.DecimalField(label='Цена', max_digits=7, decimal_places=2, min_value=0)