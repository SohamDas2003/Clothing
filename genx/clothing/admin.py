from django.contrib import admin
from clothing.models import Item, CartItem, CusOrders


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'prod_code', 'item_name', 'item_desc', 'item_price', 'category')


# Register your models here.

admin.site.register(Item, ItemAdmin)
admin.site.register(CusOrders)