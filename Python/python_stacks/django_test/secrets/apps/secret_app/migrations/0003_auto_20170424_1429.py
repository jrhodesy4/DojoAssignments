# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-24 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secret_app', '0002_auto_20170421_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='secret',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='secret_app.Secret'),
        ),
    ]