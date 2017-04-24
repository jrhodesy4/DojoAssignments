from __future__ import unicode_literals

from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publish = models.IntegerField()
    category = models.CharField(max_length=255)
    in_print = models.BooleanField(default=True)
# Create your models here.
