# Generated by Django 4.2.7 on 2023-12-23 06:57

from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_city_field_grade_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='invitation_code',
            field=models.CharField(default=users.models.get_invitation_code, max_length=20, unique=True),
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(default=0)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
            ],
        ),
    ]
