# Generated by Django 4.0.6 on 2024-04-12 11:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_advisorrequest_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisorrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 12, 15, 4, 55, 234363)),
        ),
    ]
