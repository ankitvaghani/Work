# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-23 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user_email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_pass',
            field=models.CharField(max_length=100),
        ),
    ]
