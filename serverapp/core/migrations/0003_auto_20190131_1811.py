# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-31 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190131_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='school',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
