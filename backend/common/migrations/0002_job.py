# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=128)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expires_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('industry', models.ForeignKey(related_name=b'industry', to='common.Industry')),
                ('location', models.ForeignKey(to='common.Location')),
                ('skills', models.ManyToManyField(related_name=b'skills', to='common.Skill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
