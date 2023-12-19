from django.shortcuts import render
from django.http import HttpResponse
from clothing.models import Item
from users.models import CusOrders, CusRatingFeedback

# Create your views here.

def index(request):
    itemlist = Item.objects.all()
    
    # for search functionality
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        itemlist = Item.objects.filter(item_name__icontains=item_name)
    
    context = {
        'itemlist':itemlist
    }

    return render(request, 'clothing/index.html', context)

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    
    Obj_CusOrders = CusOrders.objects.filter(
        prod_code = item.prod_code,
        user= request.user.username
    )
    
    crf = CusRatingFeedback.objects.filter(
        prod_code=item.prod_code
    )
    
    context = {
        'item':item,
        'oco':Obj_CusOrders,
        'crf':crf,
    }

    return render(request, 'clothing/detail.html', context)



def mens(request):
    itemlist = Item.objects.filter(category='m')

    # for search functionality
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        itemlist = itemlist.filter(item_name__icontains=item_name)

    context = {
        'itemlist': itemlist
    }

    return render(request, 'clothing/mens.html', context)

def womens(request):
    itemlist = Item.objects.filter(category='f')

    # for search functionality
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        itemlist = itemlist.filter(item_name__icontains=item_name)

    context = {
        'itemlist': itemlist
    }

    return render(request, 'clothing/womens.html', context)

def kids(request):
    itemlist = Item.objects.filter(category='k')

    # for search functionality
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        itemlist = itemlist.filter(item_name__icontains=item_name)

    context = {
        'itemlist': itemlist
    }

    return render(request, 'clothing/kids.html', context)