# Generated by Django 4.0.6 on 2024-04-12 11:09

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='expire_date',
            field=models.DateTimeField(default=users.models.get_today),
        ),
    ]