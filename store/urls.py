from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('', views.prod_list, name="all_bicycles"),
    path('<uuid:category_id>/', views.prod_list, name='bicycles_by_category'),
    path('<uuid:category_id>/<uuid:product_id>/', views.product_detail, name = 'bicycles_detail'),
    path('<uuid:category_id>/<uuid:product_id>/<uuid:sale_id>/', views.sale_detail, name = 'sales_detail'),

]
