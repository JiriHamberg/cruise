# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cruise', '0002_auto_20141014_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabin',
            name='name',
            field=models.CharField(default='testihytti', max_length=200),
            preserve_default=False,
        ),
    ]
