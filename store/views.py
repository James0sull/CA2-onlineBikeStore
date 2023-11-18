from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Sale

def prod_list(request, category_id=None):
    category = None
    products = Product.objects.filter(available=True)
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category, available=True)
    return render(request, 'store/category.html', {'category':category, 'prods':products})

def product_detail(request, catgory_id, product_id):
    product = get_object_or_404(Product, catgory_id=catgory_id, id=product_id)
    return render(request, 'store/product.html',{'product':product})

def sale_detail(request, sale_id):
    sale = get_object_or_404(Sale, product_id=product_id, id=sale_id)
    return render(request, 'store/sale.html', {'sale': sale})