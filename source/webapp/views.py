from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Product
from webapp.forms import ProductForm
from django.urls import reverse, reverse_lazy
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


class ProductCreate(CreateView):
    model = Product
    template_name = 'product_create.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product', kwargs={'id': self.object.id})


class ProductUpdate(UpdateView):
    template_name = 'product_update.html'
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('product', kwargs={'id': self.object.id})


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