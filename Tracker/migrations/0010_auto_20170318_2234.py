# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-18 17:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0009_auto_20170318_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mgroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tracker.group'),
        ),
    ]