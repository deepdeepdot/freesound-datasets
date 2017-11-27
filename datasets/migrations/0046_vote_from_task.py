# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-21 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0045_auto_20171116_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='from_task',
            field=models.CharField(choices=[('BE', 'Beginner'), ('AD', 'Advanced')], default='AD', max_length=2),
        ),
    ]