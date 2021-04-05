from django import forms
from webapp.models import Product, Basket, Booking


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'quantity', 'price']


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти')


class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ['quantity']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'tel', 'adrese']