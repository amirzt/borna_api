# Generated by Django 4.0.6 on 2024-04-01 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_remove_lesson_field'),
        ('content', '0004_alter_exam_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='grade',
        ),
        migrations.AddField(
            model_name='exam',
            name='lesson',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson'),
        ),
    ]
