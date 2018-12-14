# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-12-14 08:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('task', models.TextField()),
                ('pay', models.FloatField()),
                ('receiver', models.CharField(max_length=20)),
                ('status', models.BooleanField(default=False)),
                ('img', models.ImageField(upload_to=b'')),
                ('pusher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
