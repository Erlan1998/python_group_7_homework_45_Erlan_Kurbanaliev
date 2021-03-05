from django.shortcuts import render, redirect, get_object_or_404


from webapp.models import Product, category_choices
from webapp.forms import ProductForm


def index_view(request):
    product = Product.objects.all()
    return render(request, 'index.html', context={'products': product})

def product_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_view.html', context={'product': product})

def product_add_view(request):
    if request.method == 'GET':
        product = ProductForm()
        return render(request, 'add_view.html', context={'form': product})
    elif request.method == 'POST':
        product = ProductForm(data=request.POST)
        if product.is_valid():
            product = Product.objects.create(
                name=product.cleaned_data.get('name'),
                description=product.cleaned_data.get('description'),
                category=product.cleaned_data.get('category'),
                quantity=product.cleaned_data.get('quantity'),
                price=product.cleaned_data.get('price')
            )
            return redirect('product', id=product.id)
        return render(request, 'add_view.html', context={'product': product})