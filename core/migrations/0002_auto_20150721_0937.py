# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='ActSubscrita',
        ),
        migrations.AddField(
            model_name='usuario',
            name='All_day',
            field=models.BooleanField(default=False, verbose_name='All day'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='End',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 9, 37, 49, 74920, tzinfo=utc), verbose_name='End'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 9, 37, 59, 951650, tzinfo=utc), verbose_name='Start'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='Title',
            field=models.CharField(max_length=200, verbose_name='Title', blank=True),
        ),
    ]
