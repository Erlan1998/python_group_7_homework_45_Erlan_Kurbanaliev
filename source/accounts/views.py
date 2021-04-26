from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.db.models import Q
from django.views.generic import ListView
from accounts.forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.utils.http import urlencode
from webapp.forms import SearchForm
from webapp.models import Basket, Product, Booking


def register_view(request, *args, **kwargs):
    context = {}
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index_all')
    context['form'] = form
    return render(request, 'registration/register.html', context=context)


class MyLogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        cart = self.request.session.get('cart', [])

        baskets = Basket.objects.filter(pk__in=cart)
        if baskets:
            for basket in baskets:
                print(basket)
                product = Product.objects.get(pk=basket.product.pk)
                product.quantity += basket.quantity
                product.save()
                basket.delete()
        return super().dispatch(request, *args, **kwargs)


class BookingView(ListView):
    template_name = 'booking_view.html'
    model = Booking
    context_object_name = 'bookings'
    ordering = ('name',)

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(BookingView, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user__id=self.request.user.id)
        if self.search_data:
            queryset = queryset.filter(
                Q(name__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['search_form'] = self.form

        if self.search_data:
            kwargs['query'] = urlencode({'search_value': self.search_data})

        return kwargs