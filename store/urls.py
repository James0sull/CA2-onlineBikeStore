from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('', views.bike_list, name="all_bikes"),
    path('all_brands/', views.all_brands, name="all_brands"),
    path('<uuid:brand_id>/', views.brand_list, name='brands'),
    path('brand/<uuid:brand_id>/', views.brand_detail, name='brand_detail'),
    path('<uuid:brand_id>/<uuid:bike_id>/', views.bike_detail, name='bike_detail'),
    path('<uuid:brand_id>/<uuid:bike_id>/<uuid:sale_id>/', views.sale_detail, name='sale_detail'),
]

