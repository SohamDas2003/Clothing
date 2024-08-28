from django.contrib import admin
from clothing.models import Item, CartItem, CusOrders


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'item_desc', 'item_price', 'category')


# Register your models here.

admin.site.register(Item, ItemAdmin)
admin.site.register(CusOrders)
admin.site.register(CartItem)