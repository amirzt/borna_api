import datetime

from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from shop.models import Plan, Transaction, ZarinpalMerchantCode
from shop.serializers import GetPlansSerializer
from users.models import CustomUser, Wallet, Student

from django.http import HttpResponse
from django.shortcuts import redirect, render
import requests
import json

# from zarinpal.verifications import send_phone_consultation_verifications, send_online_class_reservation_verification
# import threading

ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"

CallbackURL = 'https://api.moshaversara.com/api/shop/verify/'


@api_view(['POST'])
@permission_classes([AllowAny])
def get_zarinpal_plan(request):
    plans = Plan.objects.filter(is_available=True)
    serializer = GetPlansSerializer(plans, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_credit(request):
    transaction = Transaction(user=request.user,
                              price=request.data['price'], )
    transaction.save()

    user = CustomUser.objects.get(id=request.user.id)

    return Response({
        'purchase_url': '?merchant=' + ZarinpalMerchantCode.objects.get().merchant
                        + "&phone=" + user.phone
                        + "&amount=" + str(transaction.price)
                        + "&description=" + 'افزایش موجودی'
                        + "&transaction_id=" + str(transaction.id)
    },
        status=status.HTTP_200_OK)


def send_request(request):
    req_data = {
        "merchant_id": request.GET['merchant'],
        "amount": int(request.GET['amount']),
        "callback_url": CallbackURL,
        "description": request.GET['description'],
        "metadata": {"mobile": request.GET['phone']},
    }
    req_header = {"accept": "application/json",
                  "content-type": "application/json'"}
    req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
        req_data), headers=req_header)
    authority = req.json()['data']['authority']

    transaction = Transaction.objects.get(id=request.GET['transaction_id'])
    transaction.gateway = authority
    transaction.save()

    if len(req.json()['errors']) == 0:
        return redirect(ZP_API_STARTPAY.format(authority=authority))
    else:
        e_code = req.json()['errors']['code']
        e_message = req.json()['errors']['message']
        return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")


def verify(request):
    # t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    print(request.GET.get('Status'))

    if request.GET.get('Status') == 'OK':

        transaction = Transaction.objects.get(gateway=t_authority)

        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req_data = {
            "merchant_id": ZarinpalMerchantCode.objects.get().merchant,
            "amount": transaction.price,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        print(req.json()['errors'])
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']

            print(t_status)

            if t_status == 100:
                # save reservation

                transaction.tracking_code = req.json()['data']['ref_id']
                transaction.status = Transaction.Status.SUCCESS
                transaction.save()

                # add credit
                wallet = Wallet.objects.get(student__user=transaction.user)
                wallet.balance += transaction.price
                wallet.save()

                context = {
                    'tracking_code': transaction.tracking_code
                }
                return render(request, 'successful_payment.html', context)
                # return HttpResponse('Transaction success.\nRefID: ' + str(
                #     req.json()['data']['ref_id']
                # ))
            elif t_status == 101:
                context = {
                    'tracking_code': transaction.tracking_code
                }
                return render(request, 'successful_payment.html', context)
                # return HttpResponse('Transaction submitted : ' + str(
                #     req.json()['data']['message']
                # ))
            else:
                return render(request, 'error_payment.html')

                # return HttpResponse('Transaction failed.\nStatus: ' + str(
                #     req.json()['data']['message']
                # ))
        else:
            return render(request, 'error_payment.html')

            # e_code = req.json()['errors']['code']
            # e_message = req.json()['errors']['message']
            # return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        return render(request, 'error_payment.html')

        # return HttpResponse('Transaction failed or canceled by user')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_plan(request):
    wallet = Wallet.objects.get(student__user=request.user)
    plan = Plan.objects.get(id=request.data['plan'])

    if plan.price > wallet.balance:
        return Response(status=status.HTTP_402_PAYMENT_REQUIRED, data={"message": "اعتبار حساب شما کافی نیست"})
    else:
        student = Student.objects.get(user=request.user)
        if student.expire_date < timezone.now():
            student.expire_date = timezone.now() + datetime.timedelta(days=int(plan.duration))
        else:
            student.expire_date += datetime.timedelta(days=int(plan.duration))
        student.save()

        wallet.balance -= plan.price
        wallet.save()

        return Response(status=status.HTTP_200_OK)
