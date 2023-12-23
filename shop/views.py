import datetime

from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from shop.models import Plan
from shop.serializers import GetPlansSerializer, AddTransactionSerializer
from users.models import CustomUser


@api_view(['POST'])
@permission_classes([AllowAny])
def get_zarinpal_plan(request):
    plans = Plan.objects.filter(is_available=True)
    serializer = GetPlansSerializer(plans, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_bazar_myket_order(request):
    plan = Plan.objects.get(id=request.data['plan'])
    # package_name = CustomUser.objects.get(id=request.user.id).package_name

    serializer = AddTransactionSerializer(data=request.data,
                                          context={'user': request.user,
                                                   # 'package_name': package_name,
                                                   'duration': plan.duration,
                                                   'price': plan.price,
                                                   'gateway': request.data['gateway'],
                                                   'gateway_code': request.data['gateway_code'],
                                                   'description': 'خرید اشتراک ' + plan.title})
    if serializer.is_valid():
        transaction = serializer.save()
        transaction.state = 'success'
        transaction.save()

        user = CustomUser.objects.get(id=request.user.id)
        if user.expire_date < timezone.now():
            user.expire_date = timezone.now() + datetime.timedelta(days=int(plan.duration))
        else:
            user.expire_date += datetime.timedelta(days=int(plan.duration))
        user.save()
        #
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
