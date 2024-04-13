# Generated by Django 4.0.6 on 2024-04-13 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_advisorrequest_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='max_question',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='grade',
            name='max_test',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='grade',
            name='max_time',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='grade',
            name='test_score',
            field=models.IntegerField(default=0),
        ),
    ]
