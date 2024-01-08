from django.shortcuts import render
from django.http import HttpResponse
from clothing.models import Item
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from clothing.models import Item, CartItem, CusOrders
from django.contrib import messages

# Create your views here.

def index(request):
    itemlist = Item.objects.all()
    
    # for search functionality
    item_name = request.POST.get('item_name')
    if item_name != '' and item_name is not None:
        itemlist = Item.objects.filter(item_name__icontains=item_name)
    else:
        itemlist = Item.objects.all()
        
    context = {
        'itemlist':itemlist
    }
    
    if not itemlist:
        messages.info(request, 'No search results found.')
        
    return render(request, 'clothing/index.html', context)

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    
    Obj_CusOrders = CusOrders.objects.filter(
        user= request.user.username
    )
    
    context = {
        'item':item,
        'oco':Obj_CusOrders,
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

@login_required
def Orders(request):
    user = request.user

    if request.method == 'POST':
        Obj_CusOrds = CusOrders(
            user=user,
            quantity=request.POST.get('qty'),
            size=request.POST.get('size')
        )
        Obj_CusOrds.save()

    else:
        previous_orders = CusOrders.objects.filter(user=user)
        context = {'previous_orders': previous_orders}
        return render(request, 'clothing/myorders.html', context)



def add_to_cart(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        selected_size = request.POST.get('size')
        quantity = int(request.POST.get('qty', 1))

        if request.user.is_authenticated:
            cart_item, created = CartItem.objects.get_or_create(
                user=request.user, item=item, size=selected_size
            )

            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity

            cart_item.save()

        return redirect('clothing:cart_view')

    return redirect('clothing:cart_view')


def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user).select_related('item')

    grand_total = sum(cart_item.item.item_price * cart_item.quantity for cart_item in cart_items)

    for cart_item in cart_items:
        cart_item.total_price = cart_item.item.item_price * cart_item.quantity

    return render(request, 'clothing/cart.html', {'cart_items': cart_items, 'grand_total': grand_total})


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)

    if request.user == cart_item.user:
        cart_item.delete()

    return redirect('clothing:cart_view')
