# Generated by Django 4.0.6 on 2024-04-28 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_grade_test_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='end_week_max_time',
            field=models.FloatField(default=0),
        ),
    ]
