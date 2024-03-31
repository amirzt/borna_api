from django.db import models

# Create your models here.
from users.models import Grade, Field


class ContentCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=False, null=False)
    image = models.ImageField(upload_to='content/category', blank=True, null=True)

    def __str__(self):
        return self.name


class Content(models.Model):
    class TypeChoices(models.TextChoices):
        VIDEO = 'video'
        AUDIO = 'audio'

    type = models.CharField(max_length=100, blank=False, null=False, default=TypeChoices.VIDEO,
                            choices=TypeChoices.choices)
    category = models.ForeignKey(ContentCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    subtitle = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    preview_image = models.ImageField(upload_to='content/preview', blank=True, null=True, )
    content = models.FileField(upload_to='content/file', blank=True, null=True)

    def __str__(self):
        return self.title


class Exam(models.Model):
    class ExamType(models.TextChoices):
        test = 'test'
        question = 'question'

    type = models.CharField(max_length=100, blank=False, null=False, default=ExamType.test, choices=ExamType.choices)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    # field = models.ForeignKey(Field, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    subtitle = models.CharField(max_length=100, null=False, blank=False)
    file = models.FileField(upload_to='content/exam', blank=True, null=True)
