from django.shortcuts import render, redirect, get_object_or_404


from webapp.models import Product, category_choices
from webapp.forms import ProductForm


def index_view(request):
    product = Product.objects.all()
    return render(request, 'index.html', context={'products': product})

def product_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_view.html', context={'product': product})
