# Generated by Django 5.0.4 on 2024-06-15 09:39

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_contentcategory_is_clone'),
        ('users', '0016_advisor_comment_partnership'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentcategory',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='contentcategory',
            name='discount_expire_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='contentcategory',
            name='preview_description',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='contentcategory',
            name='preview_image',
            field=models.FileField(default=None, null=True, upload_to='content/category'),
        ),
        migrations.AddField(
            model_name='contentcategory',
            name='preview_video',
            field=models.FileField(default=None, null=True, upload_to='content/category'),
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.contentcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, max_length=1000)),
                ('file', models.FileField(upload_to='content/comment/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.contentcategory')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
            ],
        ),
    ]
