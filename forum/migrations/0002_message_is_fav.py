# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-03 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_fav',
            field=models.BooleanField(default=False),
        ),
    ]
