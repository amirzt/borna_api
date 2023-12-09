from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from lessons.models import Lesson
from lessons.serializers import LessonSerializer
from users.models import Student


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_lessons(request):
    student = Student.objects.get(user=request.user)
    lesson = Lesson.objects.filter(grade=student.grade,
                                   field=student.field)
    serializer = LessonSerializer(lesson, many=True)
    return Response(serializer.data)

