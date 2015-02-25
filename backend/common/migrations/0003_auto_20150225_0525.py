# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industry',
            name='name',
            field=models.CharField(unique=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='job',
            name='expires_on',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(unique=True, max_length=128),
        ),
    ]
