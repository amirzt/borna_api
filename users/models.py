from datetime import datetime, timedelta

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.crypto import get_random_string

from users.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class AppType(models.TextChoices):
        bazar = 'bazar'
        myket = 'myket'
        googleplay = 'googleplay'
        web = 'web'
        ios = 'ios'

    phone = models.CharField(max_length=11, null=False, blank=False, unique=True)

    is_student = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joint = models.DateField(auto_now_add=True)

    app_type = models.CharField(default=AppType.bazar, choices=AppType.choices, max_length=20)
    version = models.CharField(default='0.0.0', max_length=20)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone


class Grade(models.Model):
    title = models.CharField(max_length=30, blank=False)
    code = models.CharField(max_length=3, default='', null=False)
    max_time = models.FloatField(default=0)
    end_week_max_time = models.FloatField(default=0)
    max_test = models.IntegerField(default=0)
    max_question = models.IntegerField(default=0)
    test_score = models.FloatField(default=0)

    def __str__(self):
        return self.title


class Field(models.Model):
    title = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.title


def get_student_code(grade):
    chars = '1234567890'
    random_code = get_random_string(length=4, allowed_chars=chars)
    code = "402" + grade + random_code
    return code


def get_invitation_code():
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    code = get_random_string(length=8, allowed_chars=chars)
    return code


def get_otp():
    chars = '0123456789'
    code = get_random_string(length=4, allowed_chars=chars)
    return code


def get_today():
    return datetime.now() + timedelta(days=90)


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50, null=True, blank=False)
    last_name = models.CharField(max_length=50, null=True, blank=False)

    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    # field = models.ForeignKey(Field, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    student_code = models.CharField(max_length=20, null=True, blank=True)
    invitation_code = models.CharField(max_length=20, null=False, blank=False, unique=True, default=get_invitation_code)
    image = models.ImageField(upload_to='user/image', null=True)
    expire_date = models.DateTimeField(default=get_today)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + "-" + self.grade.title


class Wallet(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.student.first_name


class Banner(models.Model):
    image = models.ImageField(upload_to='home/banner', null=False, blank=False)
    url = models.URLField(null=False, blank=False)
    is_active = models.BooleanField(default=True)


class TutorialVideo(models.Model):
    file = models.FileField(upload_to='home/tutorial', null=False, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.title


class University(models.Model):
    name = models.TextField(max_length=100, null=False, blank=False)
    logo = models.ImageField(upload_to='university')
    url = models.URLField(null=False)

    def __str__(self):
        return self.name


class UniversityTarget(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)


class AdvisorRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=11, null=False, blank=False, )
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, default=None, null=True)
    date = models.DateTimeField(default=datetime.now)
    is_called = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student


class OTP(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, null=False, blank=False, default=get_otp)
    created_at = models.DateField(auto_now_add=True)
