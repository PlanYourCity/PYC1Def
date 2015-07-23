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
        migrations.AddField(
            model_name='actempleo',
            name='Imagen',
            field=models.CharField(default=datetime.datetime(2015, 7, 23, 11, 34, 25, 106308, tzinfo=utc), max_length=800),
            preserve_default=False,
        ),
    ]
