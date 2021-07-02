from django.db import models
from django.conf import settings


class ShoeSize(models.Model):
    uk_size = models.DecimalField(max_digits=3, decimal_places=1)
    def __str__(self):
        return str(self.uk_size)

class Shoe(models.Model):
    reference = models.CharField(max_length=60)
    brand = models.CharField(max_length=60)
    available_sizes = models.ManyToManyField(ShoeSize, related_name='shoe_sizes')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.FileField(null=True, default=None)

    def __str__(self):
        return self.reference

    def get_photo_url(self):
        return settings.STATIC_URL + self.photo.name


class Order(models.Model):
    order_id = models.CharField(max_length=60)
    client = models.CharField(max_length=60)
    shoe_reference = models.ForeignKey(Shoe, on_delete=models.SET_NULL, null=True, default=None)
    size = models.ForeignKey(ShoeSize, on_delete=models.SET_NULL, null=True, default=None)
    def __str__(self):
        return self.order_id
