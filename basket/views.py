from django.shortcuts import redirect, render, get_object_or_404
from store.models import Bike
from .models import Basket, BasketItem
from django.core.exceptions import ObjectDoesNotExist

def _basket_id(request):
    basket = request.session.session_key
    if not basket:
        basket = request.session.create()
    return basket

def add_basket(request, bike_id):
    bike = get_object_or_404(id=bike_id)

    try:
        basket = Basket.objects.get(basket_id=_basket_id(request))
    except Basket.DoesNotExist:
        basket = Basket.objects.create(basket_id=_basket_id(request))
        basket.save()

    try:
        basket_items = BasketItem.objects.get(bike=bike, basket=basket)
        if basket_items.quantity < bike.stock:
            basket_items.quantity += 1
            basket_items.save()
    except BasketItem.DoesNotExist:
        basket_items = BasketItem.objects.create(bike=bike, quantity=1, basket=basket)

    return redirect('basket:basket_detail')

def basket_detail(request, total=0, counter=0, basket_items = None):
    try:
        basket = Basket.objects.get(basket_id= _basket_id(request))
        basket_items =  Basket.objects.filter(basket=basket, active=True)
        for basket_item in basket_items:
            total += (basket_item.bike.price * basket_item.quantity)
            counter += basket_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'basket.html', {'basket_items':basket_items, 'total':total, 'counter':counter})

def basket_remove(request, bike_id):
    basket= Basket.objects.get(basket_id=_basket_id(request))
    bike = get_object_or_404(Bike, id=bike_id)
    basket_item = Basket.objects.get(bike=bike, basket=basket)
    if basket_item.quantity > 1:
        basket_item.quantity -= 1
        basket_item.save()
    else:
        basket_item.delete()
    return redirect('basket:basket_detail')

def full_remove(request, bike_id):
    basket = Basket.objects.get(basket_id=_basket_id(request))
    bike = get_object_or_404(Bike, id=bike_id)
    basket_item = Basket.objects.get(bike=bike, basket=basket)
    basket_item.delete()
    return redirect('basket:basket_detail')