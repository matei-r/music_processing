# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('composer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='nr_of_songs',
            field=models.IntegerField(default=0, max_length=15),
        ),
    ]
