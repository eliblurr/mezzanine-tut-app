# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-21 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]