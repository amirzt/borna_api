# Generated by Django 4.0.6 on 2024-04-12 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_grade_code_alter_student_student_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisorrequest',
            name='grade',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.grade'),
        ),
    ]