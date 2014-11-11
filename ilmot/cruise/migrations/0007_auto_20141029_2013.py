# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cruise', '0006_auto_20141026_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabin',
            name='name',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
