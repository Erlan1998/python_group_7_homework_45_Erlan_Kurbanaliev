from rest_framework import serializers
from webapp.models import Booking, BookingProduct


class OrderBooking(serializers.ModelSerializer):
    class Meta:
        model = BookingProduct
        fields = ('id', 'product', 'booking', 'quantity')
        read_only_fields = ('booking',)


class OrderSerializer(serializers.ModelSerializer):
    BookingProduct = OrderBooking(many=True)

    class Meta:
        model = Booking
        fields = ('id', 'name', 'tel', 'adrese', 'created_at', 'user', 'BookingProduct')
        read_only_fields = ('user', 'id')

    def create(self, validated_data):
        minus_data = validated_data.pop('BookingProduct')
        creat_new = Booking.objects.create(**validated_data)
        for data in minus_data:
            w = BookingProduct(
                product=data['product'],
                booking=creat_new,
                quantity=data['quantity']
            )
            w.save()
        validated_data['BookingProduct'] = minus_data
        return validated_data
