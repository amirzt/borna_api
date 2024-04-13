from django.db import models

# Create your models here.
from users.models import Student


class LeagueItem(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    rank = models.IntegerField()
    score = models.FloatField()
    time = models.CharField(max_length=10, default='')
    question = models.IntegerField(default=0)
    test = models.IntegerField(default=0)
