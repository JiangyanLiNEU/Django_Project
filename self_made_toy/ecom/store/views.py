from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from .models import Item
from .models import Cart
# Get all models and display


def index(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'store/index.html', context)


def show(request, id):
    item = Item.objects.get(id=id)
    # return HttpResponse(item.name)
    ha = Cart.objects.filter(buy_item=item)
    if not ha:
        Cart.objects.create(buy_item=item)
    else:
        current_number = Cart.objects.get(buy_item=item).quantity
        Cart.objects.get(buy_item=item).delete()
        Cart.objects.create(buy_item=item, quantity=current_number+1)
    return cart(request)


def delete(request, id):
    item = Item.objects.get(id=id)
    Cart.objects.get(buy_item=item).delete()
    return cart(request)


def increase(request, id):
    item = Item.objects.get(id=id)
    num = Cart.objects.get(buy_item=item).quantity
    Cart.objects.get(buy_item=item).delete()
    Cart.objects.create(buy_item=item, quantity=num+1)
    return cart(request)


def decrease(request, id):
    item = Item.objects.get(id=id)
    num = Cart.objects.get(buy_item=item).quantity
    Cart.objects.get(buy_item=item).delete()
    Cart.objects.create(buy_item=item, quantity=num-1)
    return cart(request)


def cart(request):
    display = Cart.objects.all()
    context = {'displays': display}
    return render(request, 'store/cart.html', context)


# def addToCart(request, id):
#     Cart.add_to_cart(id=id)
#     Cart.save()
#     items = Cart.objects.all()
#     return render(request, 'store/test.html', {'items': items})


def detail(request, id):
    item = Item.objects.filter(id=id)
    context = {'item': item}
    return render(request, 'store/detail.html', context)
