# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cruise', '0003_cabin_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('legend', models.CharField(max_length=200)),
                ('price', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='mail',
            field=models.EmailField(default='test@test.fi', unique=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='nick_name',
            field=models.CharField(max_length=200, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='transportation',
            field=models.ForeignKey(to='cruise.Transportation'),
            preserve_default=False,
        ),
    ]
