from django.db import models
import datetime
import uuid
from django.urls import reverse

class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def get_absolute_url(self):
        return reverse('store:products_by_category', args=[self.id])
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to = 'product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, blank = True, null= True)
    updated = models.DateTimeField(auto_now=True, blank = True, null= True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.category.id, self.id])

    def __str__(self):
        return self.name

class Sale(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=0)

    class Meta:
        ordering = ('start_date',)
        verbose_name = 'sale'
        verbose_name_plural = 'sales'

    def sale_on(self):
        now = datetime.now()
        return self.start_date <= now <= self.end_date

    def __str__(self):
        return self.name