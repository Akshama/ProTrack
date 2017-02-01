# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0003_auto_20170128_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[('open', 'Open'), ('blocked', 'Blocked'), ('completed', 'Completed')], default='Open', max_length=50),
        ),
    ]