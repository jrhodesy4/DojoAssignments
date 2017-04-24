# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-18 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publish', models.IntegerField()),
                ('category', models.CharField(max_length=255)),
            ],
        ),
    ]
