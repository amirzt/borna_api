# Generated by Django 4.0.6 on 2024-03-31 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curriculumitem',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='curriculumitem',
            name='question_type',
        ),
        migrations.RemoveField(
            model_name='curriculumitem',
            name='test_type',
        ),
        migrations.AddField(
            model_name='curriculumitem',
            name='test_count',
            field=models.IntegerField(default=0),
        ),
    ]
