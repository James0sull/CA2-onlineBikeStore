from django.shortcuts import redirect, render, get_object_or_404
from store.models import Bike
from .models import Basket, BasketItem
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings 
import stripe 
from order.models import Order, OrderItem

def _basket_id(request):
    basket = request.session.session_key
    if not basket:
        basket = request.session.create()
    return basket

def add_basket(request, bike_id):
    bike = Bike.objects.get(id=bike_id)
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
        basket_items = BasketItem.objects.filter(basket=basket, active=True)
        for basket_item in basket_items:
            total += (basket_item.bike.price * basket_item.quantity)
            counter += basket_item.quantity
    except ObjectDoesNotExist:
        pass
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total * 100)
    description = 'Online Shop - New Order'
    data_key = settings.STRIPE_PUBLISHABLE_KEY
    if request.method=='POST':
        print(request.POST)
        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            billingName = request.POST['stripeBillingName']
            billingAddress1 = request.POST['stripeBillingAddressLine1']
            billingcity = request.POST['stripeBillingAddressCity']
            billingCountry = request.POST['stripeBillingAddressCountryCode']
            shippingName = request.POST['stripeShippingName']
            shippingAddress1 = request.POST['stripeShippingAddressLine1']
            shippingcity = request.POST['stripeShippingAddressCity']
            shippingCountry = request.POST['stripeShippingAddressCountryCode']
            customer = stripe.Customer.create(email=email, source=token)
            stripe.Charge.create(amount=stripe_total, currency="eur", description=description, customer=customer.id)
            try:
                order_details = Order.objects.create(
                    token = token,
                    total = total,
                    emailAddress = email,
                    billingName = billingName,
                    billingAddress1 = billingAddress1,
                    billingCity = billingcity,
                    billingCountry = billingCountry,
                    shippingName = shippingName,
                    shippingAddress1 = shippingAddress1,
                    shippingCity = shippingcity,
                    shippingCountry = shippingCountry
                    )
                order_details.save()
                for order_item in basket_items:
                    oi = OrderItem.objects.create(
                        product = order_item.product.name,
                        quantity = order_item.quantity,
                        price = order_item.product.price,
                        order = order_details)
                    oi.save

                    products = Bike.objects.get(id=order_item.product.id)
                    products.stock = int(order_item.product.stock - order_item.quantity)
                    products.save()
                    order_item.delete()
                    print('The order has been created')
                return redirect ('store:all_bikes') 
            except ObjectDoesNotExist:
                pass
        except stripe.error.CardError as e:
            return e 
    return render(request, 'basket.html', {'basket_items':basket_items, 'total':total, 'counter':counter, 'data_key':data_key, 'stripe_total':stripe_total, 'description':description})

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