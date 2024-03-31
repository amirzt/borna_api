from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from lessons.models import Lesson
from lessons.serializers import LessonSerializer
from users.models import Student


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_lessons(request):
    lesson = Lesson.objects.filter(grade=Student(user=request.user).grade)
    serializer = LessonSerializer(lesson, many=True)
    return Response(serializer.data)

