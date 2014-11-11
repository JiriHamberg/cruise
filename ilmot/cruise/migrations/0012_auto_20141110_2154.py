# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cruise', '0011_auto_20141110_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='cabin',
            field=models.ForeignKey(blank=True, to='cruise.Cabin', null=True),
        ),
    ]
