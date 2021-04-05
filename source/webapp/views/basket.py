from django.views.generic import ListView, TemplateView, CreateView
from webapp.models import Basket, Product, Booking, BookingProduct
from webapp.forms import BasketForm, BookingForm
from django.shortcuts import redirect, get_object_or_404

from django.utils.http import urlencode


class BasketIndex(ListView):
    template_name = 'baskets/index_basket.html'
    model = Basket
    context_object_name = 'baskets'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['form'] = BasketForm()
        kwargs['form_b'] = BookingForm()

        return kwargs


class CreateBasket(TemplateView):

    def post(self, request, **kwargs):
        product = Product.objects.get(pk=kwargs.get('id'))
        form = BasketForm(data=request.POST)
        if form.is_valid():
            if product.quantity >= form.cleaned_data.get('quantity'):
                try:
                    basket = Basket.objects.get(product__pk=product.pk)
                    basket.quantity += form.cleaned_data.get('quantity')
                    basket.save()

                except Basket.DoesNotExist:
                    Basket.objects.create(
                        product=product,
                        quantity=form.cleaned_data.get('quantity')
                    )
                product.quantity -= form.cleaned_data.get('quantity')
                product.save()

        return redirect('index_all')


class DeleteBasket(TemplateView):

    def post(self, request, **kwargs):
        basket = get_object_or_404(Basket, id=kwargs.get('id'))
        form = BasketForm(data=request.POST)
        if form.is_valid():
            if basket.quantity > form.cleaned_data.get('quantity'):
                product = basket.product
                product.quantity += form.cleaned_data.get('quantity')
                product.save()
                basket.quantity -= form.cleaned_data.get('quantity')
                basket.save()
            elif basket.quantity == form.cleaned_data.get('quantity'):
                product = basket.product
                product.quantity += form.cleaned_data.get('quantity')
                product.save()
                basket.delete()

        return redirect('index_basket')


class BookingCreate(CreateView):
    model = Booking
    template_name = 'baskets/index_basket.html'
    form_class = BookingForm

    def form_valid(self, form):
        booking = form.save()
        for b in Basket.objects.all():
            BookingProduct.objects.create(
                product=b.product,
                booking=booking,
                quantity=b.quantity
            )
            b.delete()
        return redirect('index_all')
