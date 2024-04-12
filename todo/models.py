from django.db import models

# Create your models here.
from lessons.models import Lesson
from users.models import Student


class Task(models.Model):
    class Priority(models.TextChoices):
        low = 'low'
        medium = 'medium'
        high = 'high'
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    time = models.IntegerField(default=0)
    is_done = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, default=None)
    priority = models.CharField(choices=Priority.choices, max_length=100, default=Priority.low)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
