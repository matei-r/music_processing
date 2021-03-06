# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-24 10:18
from __future__ import unicode_literals

import composer.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('composer', '0005_remove_song_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='name',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='song',
            name='file',
            field=models.FileField(upload_to='songs/', validators=[composer.validators.validate_file_extension]),
        ),
    ]
