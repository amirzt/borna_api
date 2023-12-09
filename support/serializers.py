from rest_framework import serializers

from support.models import FrequentlyAskedQuestion


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequentlyAskedQuestion
        fields = '__all__'
