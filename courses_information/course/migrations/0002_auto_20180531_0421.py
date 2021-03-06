# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-31 04:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
        ('lecture', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='lecture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lecture.Lecture'),
        ),
        migrations.AddField(
            model_name='course',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='room.Room'),
        ),
    ]
