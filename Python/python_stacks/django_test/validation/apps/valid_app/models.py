from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def validate(self,data):
        errors = []
        if len(data['name']) < 8:
            errors.append("Username must be at least 8 characters")
        elif len(data['name']) > 16:
            errors.append("Username can be no longer than 16 characters")
        if len(errors) == 0:
            user = User.objects.create(name=data['name'])
            return {'user': user, 'errors': None}
        else:
            return {'user': None, 'errors': errors}
class User(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


# Create your models here.
