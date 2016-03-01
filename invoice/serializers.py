from rest_framework import serializers

from invoice.models import Invoice, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('product', 'quantity', 'price')


class InvoiceSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ('customer' ,'transactions')

    def create(self, validated_data, method):
        transactions_data = validated_data.pop('transactions')
        validated_data['total_quantity'] = 0
        validated_data['total_amount'] = 0


class TransactionGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'product', 'quantity', 'price','line_total' )


class InvoiceGetSerializer(serializers.ModelSerializer):
    transactions = TransactionGetSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ('id','customer', 'total_quantity', 'total_amount', 'transactions')        