from django.db import models
from store.models import Bike

class Basket(models.Model):
    basket_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Basket'
        ordering = ['date_added']

    def __str__(self):
        return self.basket_id

class BasketItem(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Basket_Item'

    def sub_total(self):
        return self.bike.price * self.quantity

    def __str__(self):
        return self.bike
