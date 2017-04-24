from __future__ import unicode_literals

from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    


# Create your models here.
