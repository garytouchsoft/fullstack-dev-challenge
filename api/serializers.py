from rest_framework import serializers

from .models import ShoeSize, Shoe, Order

class ShoeSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeSize
        fields = ('id', 'uk_size')

class ShoeSerializer(serializers.ModelSerializer):
    available_sizes = ShoeSizeSerializer(many=True)
    class Meta:
        model = Shoe
        fields = ('id', 'reference', 'brand', 'available_sizes', 'price')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'order_id', 'client', 'shoe_reference', 'size')
