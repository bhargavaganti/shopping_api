from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from item.models import Item, Review
from  item.serializers import (ItemSerializer)


@api_view(["GET", 'POST'])
def item_list(request):
    """
        list of all items  or create new item
        """

    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        data = request.data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
