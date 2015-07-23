# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150721_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='end',
            field=models.DateTimeField(null=True, verbose_name='End'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='start',
            field=models.DateTimeField(null=True, verbose_name='Start'),
        ),
    ]
