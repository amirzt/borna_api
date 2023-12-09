from django.db import models


# Create your models here.
class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
