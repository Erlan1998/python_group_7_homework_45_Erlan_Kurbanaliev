from django.shortcuts import render


from webapp.models import Product, category_choices
from webapp.forms import ProductForm


def products_view(request):
    product = Product.objects.all()
    return render(request, 'index.html', context={'products': product})
