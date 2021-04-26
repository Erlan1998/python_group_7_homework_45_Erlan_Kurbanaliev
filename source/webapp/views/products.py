from django.contrib.auth.mixins import PermissionRequiredMixin

from webapp.models import Product
from webapp.forms import ProductForm, SearchForm, BasketForm
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode


class ProductsAll(ListView):
    template_name = 'products/index.html'
    model = Product
    context_object_name = 'products'
    ordering = ('name', 'category')
    paginate_by = 5
    paginate_orphans = 2

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(ProductsAll, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(name__icontains=self.search_data) |
                Q(description__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['search_form'] = self.form
        kwargs['form'] = BasketForm
        if self.search_data:
            kwargs['query'] = urlencode({'search_value': self.search_data})

        return kwargs


class ProductView(DetailView):
    template_name = 'products/product_view.html'
    model = Product
    pk_url_kwarg = "id"


class ProductCreate(PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'products/product_create.html'
    form_class = ProductForm
    permission_required = 'webapp.add_product'

    def get_success_url(self):
        return reverse('product', kwargs={'id': self.object.id})


class ProductUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'products/product_update.html'
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    pk_url_kwarg = 'id'
    permission_required = 'webapp.change_product'

    def get_success_url(self):
        return reverse('product', kwargs={'id': self.object.id})


class ProductDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'products/product_delete.html'
    model = Product
    context_object_name = 'product'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('index_all')
    permission_required = 'webapp.delete_product'
