# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cruise', '0005_auto_20141026_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='access_key',
            field=models.CharField(default=b'', max_length=30, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='access_key_expires_at',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
            preserve_default=True,
        ),
    ]
