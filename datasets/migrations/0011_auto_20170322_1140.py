# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0010_auto_20170322_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasetrelease',
            name='processing_last_updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
