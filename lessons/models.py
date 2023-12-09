from django.db import models

# Create your models here.
from users.models import Grade, Field


class Lesson(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=False)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=100, null=False)