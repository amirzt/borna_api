from django.db import models


# Create your models here.
from users.models import CustomUser


class Transaction(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING'
        SUCCESS = 'SUCCESS'
        FAILED = 'FAILED'

    class PaymentMethod(models.TextChoices):
        direct = 'direct'
        gift = 'gift'
        GOOGLE_PAY = 'GOOGLE_PAY'
        bazar = 'bazar'
        myket = 'myket'

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    status = models.CharField(max_length=20, default=Status.PENDING, choices=Status.choices)
    payment_method = models.CharField(max_length=20, default=PaymentMethod.direct, choices=PaymentMethod.choices)
    tracking_code = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True, max_length=1000)
    gateway = models.CharField(max_length=50, null=True, blank=True)


class Plan(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    is_available = models.BooleanField(default=True)
    duration = models.IntegerField(null=False, blank=False)
    bazar_myket = models.CharField(max_length=100, default='', null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ZarinpalMerchantCode(models.Model):
    merchant = models.CharField(max_length=100)

