# import threading

# from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# from league.calculation import job
from league.models import LeagueItem
from league.serializers import LeagueSerializer
from users.models import CustomUser
# import schedule
# import time


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


# def run_background():
#     schedule.every().days.at("04:00").do(job)
#
#     while True:
#         schedule.run_pending()
#         time.sleep(1)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def run_calculation(request):
    user = CustomUser.objects.get(id=request.user.id)

    # if user.is_superuser:
    #     if 'now' in request.data:
    #         thread = threading.Thread(target=job)
    #         thread.setDaemon(True)
    #         thread.start()
    #     else:
    #         thread = threading.Thread(target=run_background)
    #         thread.setDaemon(True)
    #         thread.start()
    #     return Response(status=status.HTTP_200_OK, data={"message": "با موفقیت انجام شد"})
    #
    # else:
    #     return Response(status=status.HTTP_403_FORBIDDEN, data={"message": "شما اجازه دسترسی به این بخش را ندارید"})
