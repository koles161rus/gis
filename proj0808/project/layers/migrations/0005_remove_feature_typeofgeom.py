# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-08 07:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0004_feature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='typeOfGeom',
        ),
    ]
