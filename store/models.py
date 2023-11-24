from django.db import models
import uuid
from django.urls import reverse

class Brand(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250, unique=True)
    image = models.ImageField(upload_to = 'brand', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'brand'
        verbose_name_plural = 'brands'
    
    def get_absolute_url(self):
        return reverse('store:bikes_by_brand', args=[self.id])
    
    def __str__(self):
        return self.name
    
class Bike(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank = True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to =  'bike', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name =  'bike'
        verbose_name_plural =  'bikes'

    def get_absolute_url(self):
        return reverse('store:bike_detail', args=[self.brand.id, self.id])

    def __str__(self):
        return self.name

class Sale(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    product = models.ForeignKey (Bike, on_delete=models.CASCADE)
    image = models.ImageField(upload_to =  'bike', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('name',)
        verbose_name = 'sale'
        verbose_name_plural = 'sales'

    def get_absolute_url(self):
        return reverse('sale_detail', args=[str(self.id)])

    def __str__(self):
        return self.name