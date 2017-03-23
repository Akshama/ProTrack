# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-23 07:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0019_comment_ccreated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sprint',
            name='status',
        ),
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
        migrations.AddField(
            model_name='comment',
            name='member',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Tracker.member'),
        ),
    ]