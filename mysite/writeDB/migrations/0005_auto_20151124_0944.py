# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writeDB', '0004_address_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='address',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
