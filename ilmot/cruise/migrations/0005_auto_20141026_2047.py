# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ilmot.custom_fields


class Migration(migrations.Migration):

    dependencies = [
        ('cruise', '0004_auto_20141015_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='nick_name',
            field=ilmot.custom_fields.CharNullField(max_length=200, unique=True, null=True, blank=True),
        ),
    ]
