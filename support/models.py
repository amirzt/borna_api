from django.db import models


# Create your models here.
class FrequentlyAskedQuestion(models.Model):
    class Type(models.TextChoices):
        app = 'app'
        advisor = 'advisor'
    question = models.CharField(max_length=255)
    answer = models.TextField(max_length=1000)
    type = models.CharField(choices=Type.choices, default=Type.app, max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
