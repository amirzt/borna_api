from django.db.models import Sum
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from curriculum.models import Category, CurriculumItem
from curriculum.serializers import GetCategoriesSerializer, AddCurriculumSerializer, GetCurriculumSerializer
from users.models import Student


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_categories(request):
    categories = Category.objects.all()
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
    item = CurriculumItem.objects.get(id=request.data['id'])
    item.delete()
    return Response({'message': 'deleted'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_time_by_date(request):
    response = {}
    items = CurriculumItem.objects.filter(student=Student.objects.get(user=request.user),
                                          date__gte=request.data['start_date'],
                                          date__lte=request.data['end_date'])
    for item in items:
        same_date = items.filter(
            date=item.date)
        response[item.date.strftime('%Y-%m-%d')] = same_date.aggregate(Sum('time'))
    sums = sorted(response.items(), key=lambda x: x[0], reverse=False)
    return Response(sums)

