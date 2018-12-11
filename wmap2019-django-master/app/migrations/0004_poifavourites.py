# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-28 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20181121_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='POIFavourites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poiID', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=80)),
                ('latitude', models.CharField(max_length=80)),
                ('longitude', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=80)),
                ('contactNumber', models.CharField(max_length=80)),
                ('imageFileName', models.CharField(max_length=80)),
                ('lastUpdate', models.CharField(max_length=80)),
            ],
        ),
    ]