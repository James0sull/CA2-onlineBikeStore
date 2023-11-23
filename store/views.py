from django.shortcuts import render, get_object_or_404
from .models import Brand, Bike, Sale

def bike_list(request, brand_id=None):
    brand = None
    bikes = Bike.objects.filter(available=True)
    if brand_id:
        brand = get_object_or_404(brand, id=brand_id)
        bikes = Bike.objects.filter(brand=brand, available=True)
    return render(request, 'store/brand.html', {'brand':brand, 'bike':bikes})

def bike_detail(request, brand_id, bike_id):
    bike = get_object_or_404(bike, brand_id=brand_id, id=bike_id)
    return render(request, 'store/bike.html',{'bike':bike})

def sale_detail(request, sale_id):
    sale = get_object_or_404(Sale, bike_id=bike_id, id=sale_id)
    return render(request, 'store/sale.html', {'sale': sale})