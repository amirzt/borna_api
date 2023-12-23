from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from content.models import ContentCategory, Content, Exam
from content.serializers import ContentCategorySerializer, ContentSerializer, ExamSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_content_categories(request):
    categories = ContentCategory.objects.all()
    serializer = ContentCategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_content(request):
    content = Content.objects.filter(category=request.data['category'])
    serializer = ContentSerializer(content, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_exam(request):
    exams = Exam.objects.filter(grade=request.data['grade'], field=request.data['field'])
    serializer = ExamSerializer(exams, many=True)
    return Response(serializer.data)
