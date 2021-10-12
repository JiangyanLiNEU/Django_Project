from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.shortcuts import get_object_or_404

# Create your models here.


class Item(models.Model):
    name = CharField(max_length=200)
    price = IntegerField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    buy_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    # def add_to_cart(self, id):
    #     item = Item.objects.get(id=id)
    #     self.objects.create(buy_item=item, quantity=1)
