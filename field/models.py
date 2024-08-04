from django.db import models

# Create your models here.
from users.models import Grade


class FieldIntro(models.Model):
    name = models.CharField(max_length=1000, null=False, blank=False)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    banner = models.ImageField(upload_to='field/banner/', null=False)
    button = models.ImageField(upload_to='field/button/', null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FieldAudio(models.Model):
    intro = models.ForeignKey(FieldIntro, on_delete=models.CASCADE)
    file = models.FileField(upload_to='field/audio/')
    creator = models.CharField(max_length=1000, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FieldQuestion(models.Model):
    intro = models.ForeignKey(FieldIntro, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000, null=False, blank=False)
    answer = models.TextField(max_length=1000, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
