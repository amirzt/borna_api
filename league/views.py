from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from league.models import LeagueItem
from league.serializers import LeagueSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_league(request):
    league_item = LeagueItem.objects.filter(date=request.data['date']).order_by('rank')

    user_rank = LeagueItem.objects.filter(date=request.data['date'],
                                          student__user=request.user)
    return Response({
        'data': LeagueSerializer(league_item, many=True).data,
        'user_rank': user_rank.last().rank if user_rank.count() != 0 else 0
    })
