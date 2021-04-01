from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Product
from webapp.forms import ProductForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class ProductsAll(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'
    ordering = ('name', 'category')
    paginate_by = 5
    paginate_orphans = 2

class ProductView(DetailView):
    template_name = 'product_view.html'
    model = Product
    pk_url_kwarg = "id"

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


def product_update_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'GET':
        form = ProductForm(initial={
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'quantity': product.quantity,
            'price': product.price
        })
        return render(request, 'update.html', context={'form': form, 'product': product, 'category': category_choices})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = request.POST.get('name')
            product.description = request.POST.get('description')
            product.category = request.POST.get('category')
            product.quantity = request.POST.get('quantity')
            product.price = request.POST.get('price')
            product.save()
            return redirect('product', id=product.id)
        return render(request, 'add_view.html', context={'form': form, 'product': product})


def product_delete_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
    return redirect('index_all')


def search_view(request):
    name = request.GET.get('name')
    product = Product.objects.all().order_by('name').exclude(quantity=0)
    if name:
        product = product.filter(name=name)
    return render(request, 'index.html', context={'products': product})


def category_chek(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'category_view.html', context={'product': product})