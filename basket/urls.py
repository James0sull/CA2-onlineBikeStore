from django.urls import path
from . import views

app_name='basket'

urlpatterns = [
    path('add/<uuid:bike_id>/', views.add_basket, name='add_basket'),
    path('', views.basket_detail, name='basket_detail'),
    path('remove/<uuid:bike_id>/', views.basket_remove, name='basket_remove'),
    path('full_remove/<uuid:bike_id>/', views.full_remove, name='full_remove'),
]