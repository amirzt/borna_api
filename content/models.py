import datetime

from django.db import models

# Create your models here.
from lessons.models import Lesson
from users.models import Grade, Field, Student


class ContentCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=False, null=False)
    image = models.ImageField(upload_to='content/category', blank=True, null=True)
    is_special = models.BooleanField(default=False)
    is_free = models.BooleanField(default=True)
    price = models.IntegerField(default=0)
    is_clone = models.BooleanField(default=False)

    preview_video = models.FileField(upload_to='content/category', null=True, default=None)
    preview_image = models.FileField(upload_to='content/category', null=True, default=None)
    preview_description = models.TextField(max_length=1000, blank=True, null=False, default='')

    discount = models.IntegerField(default=0)
    discount_expire_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    category = models.ForeignKey(ContentCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Content(models.Model):
    class TypeChoices(models.TextChoices):
        VIDEO = 'video'
        AUDIO = 'audio'

    class OrientationChoices(models.TextChoices):
        portrait = 'portrait'
        landscape = 'landscape'

    type = models.CharField(max_length=100, blank=False, null=False, default=TypeChoices.VIDEO,
                            choices=TypeChoices.choices)
    category = models.ForeignKey(ContentCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    subtitle = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    preview_image = models.ImageField(upload_to='content/preview', blank=True, null=True, )
    content = models.FileField(upload_to='content/file', blank=True, null=True)
    orientation = models.CharField(choices=OrientationChoices.choices, default=OrientationChoices.landscape,
                                   max_length=30)

    def __str__(self):
        return self.title


class Exam(models.Model):
    class ExamType(models.TextChoices):
        test = 'test'
        question = 'question'

    type = models.CharField(max_length=100, blank=False, null=False, default=ExamType.test, choices=ExamType.choices)
    # grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    # field = models.ForeignKey(Field, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, default=1)
    title = models.CharField(max_length=100, null=False, blank=False)
    subtitle = models.CharField(max_length=100, null=False, blank=False)
    file = models.FileField(upload_to='content/exam', blank=True, null=True)


class ContentAccess(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    category = models.ForeignKey(ContentCategory, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    category = models.ForeignKey(ContentCategory, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000, null=False, blank=True)
    file = models.FileField(upload_to='content/comment/')
