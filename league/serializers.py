from rest_framework import serializers

from league.models import LeagueItem, GroupMember, LeagueGroup
from users.serializers import GetStudentInfoSerializer


class LeagueSerializer(serializers.ModelSerializer):
    student = GetStudentInfoSerializer()

    class Meta:
        model = LeagueItem
        fields = '__all__'


class AddMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMember
        fields = ['student', 'group']


class MemberSerializer(serializers.ModelSerializer):
    student = GetStudentInfoSerializer()

    class Meta:
        model = GroupMember
        fields = ['student', 'id']


class GroupSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField('get_members')
    is_creator = serializers.SerializerMethodField('get_is_creator')

    @staticmethod
    def get_members(self):
        all_members = GroupMember.objects.filter(group=self)
        return MemberSerializer(all_members, many=True).data

    def get_is_creator(self, data):
        return True if data.creator.user.id == self.context.get('user') else False

    class Meta:
        model = LeagueGroup
        fields = '__all__'
