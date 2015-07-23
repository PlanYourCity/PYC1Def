# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150721_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='actempleo',
            name='Fecha',
            field=models.CharField(default=datetime.datetime(2015, 7, 22, 6, 46, 36, 278697, tzinfo=utc), max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actempleo',
            name='Hora',
            field=models.CharField(default=datetime.datetime(2015, 7, 22, 6, 46, 47, 874754, tzinfo=utc), max_length=800),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actvivienda',
            name='Fecha',
            field=models.CharField(default=datetime.datetime(2015, 7, 22, 6, 47, 1, 989085, tzinfo=utc), max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actvivienda',
            name='Hora',
            field=models.CharField(default=datetime.datetime(2015, 7, 22, 6, 47, 16, 303216, tzinfo=utc), max_length=800),
            preserve_default=False,
        ),
    ]
