# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cruise', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentgroup',
            name='cruises',
        ),
        migrations.AddField(
            model_name='cruise',
            name='registration_end',
            field=models.DateTimeField(default=datetime.date(2014, 10, 14)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cruise',
            name='registration_start',
            field=models.DateTimeField(default=datetime.date(2014, 10, 14)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cruise',
            name='student_groups',
            field=models.ManyToManyField(to='cruise.StudentGroup'),
            preserve_default=True,
        ),
    ]
