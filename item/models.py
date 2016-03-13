from __future__ import unicode_literals

from django.db import models


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_price = models.FloatField()
    posted_by = models.CharField(max_length=100)
    number_of_items = models.IntegerField()
    item_categories = models.CharField(max_length=100)
    item_description = models.CharField(max_length=500)
    item_rating = models.IntegerField()

class Review(models.Model):
    item = models.ForeignKey(Item, related_name='reviews' ,default='')
    user_id = models.IntegerField()
    rating = models.IntegerField()
    comment = models.CharField(max_length=500)
    
    
