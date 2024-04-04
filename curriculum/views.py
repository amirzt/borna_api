from django.db.models import Sum, Avg
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from curriculum.models import CurriculumCategory, CurriculumItem
from curriculum.serializers import GetCategoriesSerializer, AddCurriculumSerializer, GetCurriculumSerializer
from league.models import LeagueItem
from users.models import Student


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_categories(request):
    categories = CurriculumCategory.objects.all()
    serializer = GetCategoriesSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_curriculum(request):
    serializer = AddCurriculumSerializer(data=request.data,
                                         context={'student': Student.objects.get(user=request.user)})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_curriculum(request):
    items = CurriculumItem.objects.filter(student=Student.objects.get(user=request.user),
                                          date=request.data['date'])
    serializer = GetCurriculumSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_curriculum(request):
    id_list = request.data.get('id_list')

    if not id_list:
        return Response({'error': 'هیچ آیدی ای ارسال نشده است'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        CurriculumItem.objects.filter(id__in=id_list).delete()
    except Exception as e:
        return Response(status=400, data={'message': str(e)})
    return Response(status=status.HTTP_200_OK, data={'message': 'با موفقیت حذف شد'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_time_by_date(request):
    response = {}
    items = CurriculumItem.objects.filter(student=Student.objects.get(user=request.user),
                                          date__gte=request.data['start_date'],
                                          date__lte=request.data['end_date'],
                                          lesson=request.data['lesson'])

    # league_items = LeagueItem.objects.filter(student=Student.objects.get(user=request.user),
    #                                       date__gte=request.data['start_date'],
    #                                       date__lte=request.data['end_date'])
    for item in items:
        same_date = items.filter(
            date=item.date)
        response[item.date.strftime('%Y-%m-%d')] = {
            'total_time': same_date.aggregate(Sum('time')),
            'total_test': same_date.aggregate(Sum('test_count')),
            'total_question': same_date.aggregate(Sum('question_count')),
            # 'league_score': league_items.aggregate(Avg('score'))
        }
    sums = sorted(response.items(), key=lambda x: x[0], reverse=False)
    return Response(sums)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_day_total(request):
    items = CurriculumItem.objects.filter(date=request.data['date'])

    total = 0
    for item in items:
        total += item.time

    return Response({"total_time": total}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def total_by_lesson(request):
    c1 = CurriculumItem.objects.filter(student=Student.objects.get(user=request.user),
                                       date__gte=request.data['s1'],
                                       date__lte=request.data['e1'])
    l1 = LeagueItem.objects.filter(student=Student.objects.get(user=request.user),
                                   date__gte=request.data['s1'],
                                   date__lte=request.data['e1'],)

    data = {
        'c1': {
            'total_test': c1.aggregate(Sum('test_count')),
            'total_question': c1.aggregate(Sum('question_count')),
            'total_time': c1.aggregate(Sum('time')),
            'clone': l1.aggregate(Sum('score'))
        }
    }
    return Response(data=data)
