# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writeDB', '0005_auto_20151124_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='address',
            field=models.CharField(max_length=255),
        ),
    ]
