from rest_framework import serializers

from shop.models import Transaction


class AddTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['price', 'payment_method']


class GetTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
