from django.urls import path, include
from clothing import views

app_name= 'clothing'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:item_id>/', views.detail, name='detail'),
    path('mens/', views.mens, name='mens'),
    path('womens/', views.womens, name='womens'),
    path('kids/', views.kids, name='kids'),
    path('orders/<int:id>/<int:pdcd>/<str:user>/', views.Orders, name='orders'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('myorders/', views.Orders, name='myorders'),
    path('orders/<int:order_id>/cancel/', views.cancel_order, name='cancel_order'),
]