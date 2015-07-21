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
            name='all_day',
            field=models.BooleanField(default=False, verbose_name='All day'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 10, 27, 50, 34213, tzinfo=utc), verbose_name='End'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 10, 27, 58, 922646, tzinfo=utc), verbose_name='Start'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title', blank=True),
        ),
    ]
