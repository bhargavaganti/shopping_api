from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from invoice.models import Invoice, Transaction
from invoice.serializers import (InvoiceSerializer,
                             TransactionSerializer,
                             TransactionGetSerializer,
                             InvoiceGetSerializer
                             )


@api_view(["GET", 'POST'])
def invoice_list(request):
    """
        list of all invoice  or create new invoice
        """

    if request.method == 'GET':
        invoices = Invoice.objects.all()

        for invoice in invoices:
            transactions = Transaction.objects.filter(invoice_id=invoice.id)
            invoice.transactions = transactions

        serializer = InvoiceGetSerializer(invoices, many=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'POST':
        serializer = InvoiceSerializer(data=request.data)
        data = request.data
        if serializer.is_valid():
            save = InvoiceSerializer(data=data)
            save.create(request.data, request.method)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)