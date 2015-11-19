# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writeDB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='aim',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='mobile',
            field=models.CharField(max_length=60, blank=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='phone',
            field=models.CharField(max_length=60, blank=True),
        ),
    ]
