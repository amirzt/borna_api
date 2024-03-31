from rest_framework import serializers

from league.models import LeagueItem


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeagueItem
        fields = '__all__'
