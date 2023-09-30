from django.urls import path, include
from clothing import views

urlpatterns = [
    path('home/', views.index, name='index'),
]