from django.db import models

from lessons.models import Lesson
from users.models import Grade, Student, Advisor


class CurriculumCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CurriculumItem(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    category = models.ForeignKey(CurriculumCategory, on_delete=models.CASCADE)
    # grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question_count = models.IntegerField(default=0)
    test_count = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    date = models.DateField(null=False, blank=False)


class AdvisorPlan(models.Model):
    advisor = models.ForeignKey(Advisor, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    category = models.ForeignKey(CurriculumCategory, on_delete=models.CASCADE)
    # grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question_count = models.IntegerField(default=0)
    test_count = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    date = models.DateField(null=False, blank=False)
