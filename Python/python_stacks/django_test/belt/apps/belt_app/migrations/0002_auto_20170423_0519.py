# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-23 05:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='f_name',
            new_name='alias',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='l_name',
            new_name='name',
        ),
    ]
