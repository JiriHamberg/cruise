# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cruise', '0010_auto_20141110_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='cabin',
            field=models.ForeignKey(to='cruise.Cabin', blank=True),
        ),
    ]
