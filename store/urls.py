from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('', views.brand_list, name="all_brands"),
    path('all_bikes/', views.bike_list, name='all_bikes'),
    path('<uuid:brand_id>/<uuid:bike_id>/', views.brand_detail, name='bike_detail'),
    path('sales/', views.all_sales, name='all_sales'),

]
