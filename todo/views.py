from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from todo.models import Task
from todo.serializers import TaskSerializer, GetTaskSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_task(request):
    serializer = TaskSerializer(data=request.data,
                                context={'user': request.user})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_tasks(request):
    tasks = Task.objects.filter(date=request.data['date'],
                                student__user=request.user)
    return Response(GetTaskSerializer(tasks, many=True).data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_tasks(request):
    id_list = request.data.get('id_list')

    if not id_list:
        return Response({'error': 'هیچ آیدی ای ارسال نشده است'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        Task.objects.filter(id__in=id_list).delete()
    except Exception as e:
        return Response(status=400, data={'message': str(e)})
    return Response(status=status.HTTP_200_OK, data={'message': 'با موفقیت حذف شد'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_task(request):
    task = Task.objects.get(id=request.data['task'])

    task.is_done = False if task.is_done else True
    task.save()
    return Response(status=status.HTTP_200_OK)
