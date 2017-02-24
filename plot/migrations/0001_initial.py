# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-23 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyWeather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField()),
                ('day', models.IntegerField()),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=5)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyWeatherByCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField()),
                ('boston_temp', models.DecimalField(decimal_places=1, max_digits=5)),
                ('houston_temp', models.DecimalField(decimal_places=1, max_digits=5)),
                ('new_york_temp', models.DecimalField(decimal_places=1, max_digits=5)),
                ('san_franciso_temp', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyWeatherSeattle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField()),
                ('seattle_temp', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
        ),
    ]