from django.contrib import admin
from clothing.models import Item, CartItem, CusOrders

# Register your models here.

admin.site.register(Item)
admin.site.register(CartItem)
admin.site.register(CusOrders)