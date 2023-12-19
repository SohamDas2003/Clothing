from django.urls import path, include
from clothing import views

app_name= 'clothing'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('detail/<int:item_id>/', views.detail, name='detail'),
    path('mens/', views.mens, name='mens'),
    path('womens/', views.womens, name='womens'),
    path('kids/', views.kids, name='kids'),
]