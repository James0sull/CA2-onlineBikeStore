from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('', views.prod_list, name="all_bikes"),
    path('<uuid:brand_id>/', views.prod_list, name='bikes_by_brand'),
    path('<uuid:brand_id>/<uuid:bike_id>/', views.bike_detail, name = 'bike_detail'),
    path('<uuid:brand_id>/<uuid:bike_id>/<uuid:sale_id>/', views.sale_detail, name = 'sale_detail'),

]
