from django.shortcuts import render, get_object_or_404
from .models import Brand, Bike, Sale
import uuid

def brand_list(request, brand_id=None):
    brand = None
    all_brands = Brand.objects.all()
    return render(request, 'store/brand.html', {'all_brands': all_brands})


def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    return render(request, 'store/brand_detail.html', {'brand': brand})


def bike_list(request, brand_id=None):
    brand = None
    bike = Bike.objects.filter(available=True)
    if brand_id:
        brand = get_object_or_404(Brand, id=brand_id)
        bike = Bike.objects.filter(brand=brand, available=True)
    return render(request, 'store/bike.html', {'brand':brand, 'bike':bike})


def bike_detail(request, brand_id, bike_id):
    try:
        brand_id = uuid.UUID(brand_id)
        bike_id = uuid.UUID(bike_id)
    except ValueError:
        raise Http404("Invalid UUID format")

    bike = get_object_or_404(Bike, brand__id=brand_id, id=bike_id)
    return render(request, 'store/bike.html',{'bike':bike})

def all_sales(request):
    all_sales = Sale.objects.all()
    return render(request, 'store/sale.html', {'all_sales': all_sales})

    
