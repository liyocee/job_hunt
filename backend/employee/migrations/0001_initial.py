# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_job'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppliedJobs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('phone_number', models.CharField(max_length=128)),
                ('industry', models.ManyToManyField(to='common.Industry')),
                ('location', models.ForeignKey(to='common.Location')),
                ('skills', models.ManyToManyField(to='common.Skill')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='appliedjobs',
            name='employee',
            field=models.ForeignKey(to='employee.Employee'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appliedjobs',
            name='job',
            field=models.ForeignKey(to='common.Job'),
            preserve_default=True,
        ),
    ]
