from rest_framework import serializers

from league.models import LeagueItem
from users.serializers import GetStudentInfoSerializer


class LeagueSerializer(serializers.ModelSerializer):
    student = GetStudentInfoSerializer()

    class Meta:
        model = LeagueItem
        fields = '__all__'
