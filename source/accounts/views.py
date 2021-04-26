from django.contrib.auth import login
from django.contrib.auth.views import LogoutView

from accounts.forms import UserRegisterForm
from django.shortcuts import render, redirect

from webapp.models import Basket, Product


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

