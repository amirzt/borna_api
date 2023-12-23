from rest_framework import serializers

from shop.models import Transaction, Plan


class GetTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class GetPlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class AddTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = []

    def save(self, **kwargs):
        transaction = Transaction(user=self.context['user'],
                                  price=self.context['price'],
                                  gateway=self.context['gateway'],
                                  gateway_code=self.context['gateway_code'],
                                  duration=self.context['duration'],
                                  description=self.context['description'])
        transaction.save()
        return transaction
