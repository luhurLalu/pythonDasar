# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-31 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nip', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'lecture',
            },
        ),
    ]
