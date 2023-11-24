from django.shortcuts import render, get_object_or_404
from .models import Brand, Bike, Sale

def brand_list(request, brand_id=None):
    brand = None
    all_brands = Brand.objects.filter(available=True)
    bike = Bike.objects.filter(available=True)
    if brand_id:
        brand = get_object_or_404(Brand, id=brand_id)
        bike = Bike.objects.filter(brand=brand, available=True)
    return render(request, 'store/brand.html', {'brand':brand, 'bike':bike})

def bike_list(request, brand_id=None):
    brand = None
    bike = Bike.objects.filter(available=True)
    if brand_id:
        brand = get_object_or_404(Brand, id=brand_id)
        bike = Bike.objects.filter(brand=brand, available=True)
    return render(request, 'store/bike.html', {'brand':brand, 'bike':bike})


def bike_detail(request, brand_id, bike_id):
    bike = get_object_or_404(Bike, brand_id=brand_id, id=bike_id)
    return render(request, 'store/bike.html',{'bike':bike})

def sale_detail(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    related_bike_id = sale.bike_id  # Replace 'bike_id' with the actual field name
    return render(request, 'store/sale.html', {'sale': sale, 'related_bike_id': related_bike_id})