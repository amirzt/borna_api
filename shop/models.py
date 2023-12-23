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
