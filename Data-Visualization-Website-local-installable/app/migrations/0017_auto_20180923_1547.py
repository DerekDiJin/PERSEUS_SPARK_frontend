# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-09-23 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_bookmark_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='analyzed_fulldata_file',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='analyzed_graph_file',
            field=models.CharField(default='', max_length=256),
        ),
    ]
