from django.shortcuts import render
from django.http import HttpResponse
from clothing.models import Item
# Create your views here.

def index(request):
    itemlist = Item.objects.all()
    return HttpResponse(itemlist)