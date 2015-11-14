# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ngo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20, blank=True)),
                ('mobile', models.CharField(max_length=20, blank=True)),
                ('email', models.CharField(max_length=100, blank=True)),
                ('website', models.CharField(max_length=100, blank=True)),
                ('person', models.CharField(max_length=100, blank=True)),
                ('purpose', models.CharField(max_length=200, blank=True)),
                ('aim', models.CharField(max_length=500, blank=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]
