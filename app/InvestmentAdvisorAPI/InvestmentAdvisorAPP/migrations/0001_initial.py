# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-12-21 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvestmentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=15)),
                ('inputA', models.IntegerField()),
                ('inputB', models.IntegerField()),
                ('inputC', models.IntegerField()),
                ('inputD', models.IntegerField()),
                ('inputE', models.IntegerField()),
                ('score', models.IntegerField()),
            ],
        ),
    ]
