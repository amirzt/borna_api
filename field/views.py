from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from field.models import FieldIntro
from field.serializers import FieldIntroSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_intro(request):
    intro = FieldIntro.objects.all()
    if 'grade' in request.data:
        intro = intro.filter(grade_id=request.data['grade'])

    return Response(FieldIntroSerializer(intro, many=True).data)
