from django.db import models

from lessons.models import Lesson
from users.models import Grade, Student


class CurriculumCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CurriculumItem(models.Model):
    class QuestionType(models.TextChoices):
        test = 'test'
        tashrihi = 'tashrihi'

    class TestType(models.TextChoices):
        test = 'test'
        exam = 'exam'

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    category = models.ForeignKey(CurriculumCategory, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question_type = models.CharField(max_length=255, choices=QuestionType.choices, default=QuestionType.test)
    question_count = models.IntegerField(default=0)
    test_type = models.CharField(max_length=255, choices=TestType.choices, default=TestType.test)
    time = models.IntegerField(default=0)
    date = models.DateField(null=False, blank=False)
