# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActEmpleo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Ciudad', models.CharField(max_length=50)),
                ('Direccion', models.CharField(max_length=200)),
                ('Titulo', models.CharField(max_length=200)),
                ('Descripcion', models.CharField(max_length=800)),
                ('Sueldo', models.CharField(max_length=10)),
                ('Periodo', models.CharField(max_length=50)),
                ('Plazas', models.CharField(max_length=800)),
                ('Usuario_owner', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ActOcio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Ciudad', models.CharField(max_length=50)),
                ('Direccion', models.CharField(max_length=200)),
                ('Titulo', models.CharField(max_length=200)),
                ('Descripcion', models.CharField(max_length=800)),
                ('Imagen', models.CharField(max_length=800)),
                ('Precio', models.CharField(max_length=800)),
                ('Fecha', models.CharField(max_length=60)),
                ('Hora', models.CharField(max_length=800)),
                ('Aforo_Max', models.CharField(max_length=800)),
                ('Usuario_owner', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ActVivienda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Ciudad', models.CharField(max_length=50)),
                ('Direccion', models.CharField(max_length=200)),
                ('Titulo', models.CharField(max_length=200)),
                ('Descripcion', models.CharField(max_length=800)),
                ('Imagen', models.CharField(max_length=800)),
                ('Precio', models.CharField(max_length=800)),
                ('NumHab', models.CharField(max_length=10)),
                ('TipoOferta', models.CharField(max_length=15)),
                ('Usuario_owner', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('User', models.CharField(max_length=100)),
                ('ActSubscrita', models.CharField(max_length=300)),
                ('Categoria', models.CharField(max_length=15)),
            ],
        ),
    ]
