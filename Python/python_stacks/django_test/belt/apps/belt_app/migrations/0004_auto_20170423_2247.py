# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-23 22:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0003_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='belt_app.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='author',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='title',
        ),
        migrations.AlterField(
            model_name='reviews',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='belt_app.User'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='book_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='belt_app.Books'),
        ),
    ]
