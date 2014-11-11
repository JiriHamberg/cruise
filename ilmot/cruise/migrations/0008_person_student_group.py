# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cruise', '0007_auto_20141029_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='student_group',
            field=models.ForeignKey(default=1, to='cruise.StudentGroup'),
            preserve_default=False,
        ),
    ]
