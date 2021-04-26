from django.urls import path
from webapp.views import (
    ProductsAll,
    ProductView,
    ProductCreate,
    ProductUpdate,
    ProductDelete,
    BasketIndex,
    CreateBasket,
    DeleteBasket,
    BookingCreate
)


urlpatterns = [
    path('', ProductsAll.as_view(), name='index_all'),
    path('product/<int:id>/', ProductView.as_view(), name='product'),
    path('product/create/', ProductCreate.as_view(), name='product_create'),
    path('product/<int:id>/update', ProductUpdate.as_view(), name='product_update'),
    path('product/<int:id>/delete', ProductDelete.as_view(), name='product_delete'),
    path('basket/', BasketIndex.as_view(), name='index_basket'),
    path('create/basket/<int:id>/', CreateBasket.as_view(), name='create_basket'),
    path('basket/delete/<int:id>/', DeleteBasket.as_view(), name='delete_basket'),
    path('booking/create/', BookingCreate.as_view(), name='booking_create'),
]