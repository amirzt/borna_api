from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from support.models import FrequentlyAskedQuestion
from support.serializers import QuestionsSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_questions(request):
    questions = FrequentlyAskedQuestion.objects.all()
    if 'type' in request.data:
        questions = questions.filter(type=request.data['type'])
    serializer = QuestionsSerializer(questions, many=True)
    return Response(serializer.data)
