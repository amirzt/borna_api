from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from league.models import LeagueItem, LeagueGroup, GroupMember
from league.serializers import LeagueSerializer, AddMemberSerializer, GroupSerializer
from users.models import Student
from users.serializers import GetStudentInfoSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_league(request):
    if 'group' in request.data:
        group = LeagueGroup.objects.get(id=request.data['group'])
        league_item = LeagueItem.objects.filter(date=request.data['date'],
                                                student__in=Student.objects.filter(groupmember__group=group)).order_by(
            'rank')

        user_rank = LeagueItem.objects.filter(date=request.data['date'],
                                              student__user=request.user)
    else:
        league_item = LeagueItem.objects.filter(date=request.data['date']).order_by('rank')

        user_rank = LeagueItem.objects.filter(date=request.data['date'],
                                              student__user=request.user)
    return Response({
        'data': LeagueSerializer(league_item, many=True).data,
        'user_rank': user_rank.last().rank if user_rank.count() != 0 else 0
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_group(request):
    group = LeagueGroup(name=request.data['name'],
                        is_public=request.data['is_public'],
                        creator=Student.objects.get(user=request.user),
                        image=request.data['image'])
    group.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_group(request):
    group = LeagueGroup.objects.get(id=request.data['group'])

    if group.creator.user.id == request.user.id:
        group.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def search_student(request):
    try:
        student = Student.objects.get(student_code=request.data['student_code'])
        serializer = GetStudentInfoSerializer(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_member(request):
    members = GroupMember.objects.filter(group_id=request.data['group'])
    if members.count() < 20:
        member = GroupMember(student=Student.objects.get(student_code=request.data['student_code']),
                             group_id=request.data['group'])
        member.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response({"message": "حداکثر تعداد اعضای یک گروه 20 نفر است"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_user(request):
    member = GroupMember.objects.get(id=request.data['id'])
    member.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_groups(request):
    student = Student.objects.get(user_id=request.user.id)
    if 'mine' in request.data:
        groups = LeagueGroup.objects.filter(groupmember__student=student)
        created = LeagueGroup.objects.filter(creator=student)
        groups = groups | created
        groups = groups.distinct()
    elif 'search' in request.data:
        groups = LeagueGroup.objects.filter(is_public=True,
                                            name__contains=request.data['search'])
    else:
        groups = LeagueGroup.objects.filter(is_public=True)

    serializer = GroupSerializer(groups, many=True,
                                 context={'user': request.user})
    return Response(serializer.data)
