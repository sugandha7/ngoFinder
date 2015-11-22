# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writeDB', '0002_auto_20151119_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='mobile',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='phone',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='purpose',
            field=models.TextField(max_length=500, blank=True),
        ),
    ]
