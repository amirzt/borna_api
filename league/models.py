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


class LeagueGroup(models.Model):
    name = models.TextField(max_length=100, null=False, blank=False)
    creator = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
    image = models.FileField(upload_to='league/group')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class GroupMember(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(LeagueGroup, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'group')
