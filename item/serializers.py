from item.models import Item, Review
from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('item_name', 'item_price', 'posted_by', 'number_of_items', 'item_categories', 'item_description', 'item_rating')