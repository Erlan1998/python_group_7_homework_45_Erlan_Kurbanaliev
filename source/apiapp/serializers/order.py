from rest_framework import serializers
from webapp.models import Booking, BookingProduct


class OrderBooking(serializers.ModelSerializer):
    class Meta:
        model = BookingProduct
        fields = ('id', 'product', 'booking', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    BookingProduct = OrderBooking(many=True)

    class Meta:
        model = Booking
        fields = ('id', 'name', 'tel', 'adrese', 'created_at', 'user', 'BookingProduct')
        read_only_fields = ('user', 'id')

    def create(self, validated_data):
        print(validated_data)
