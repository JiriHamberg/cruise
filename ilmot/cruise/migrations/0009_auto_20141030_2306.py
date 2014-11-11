# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cruise', '0008_person_student_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cabin',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cabin',
            name='student_group',
        ),
    ]
