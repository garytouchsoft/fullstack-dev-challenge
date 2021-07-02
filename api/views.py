from rest_framework import viewsets

from .serializers import ShoeSizeSerializer, ShoeSerializer, OrderSerializer
from .models import ShoeSize, Shoe, Order


class ShoeSizeViewSet(viewsets.ModelViewSet):
    queryset = ShoeSize.objects.all().order_by('uk_size')
    serializer_class = ShoeSizeSerializer

class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all().order_by('reference')
    serializer_class = ShoeSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('order_id')
    serializer_class = OrderSerializer