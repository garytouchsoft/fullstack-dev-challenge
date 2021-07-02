from django.contrib import admin

from .models import ShoeSize, Shoe, Order

admin.site.register(ShoeSize)
admin.site.register(Shoe)
admin.site.register(Order)
