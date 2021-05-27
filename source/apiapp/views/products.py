from rest_framework import viewsets
from rest_framework.views import APIView

from webapp.models import Product, Booking
from apiapp.serializers import ProductSerializer, OrderSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = OrderSerializer
