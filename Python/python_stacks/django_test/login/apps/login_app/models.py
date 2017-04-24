from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class UserManager(models.Manager):
    def register(self,data):
        errors = []
        if len(data['f_name']) < 2:
            errors.append("First name must be at least 2 characters")
        if not data['f_name'].isalpha():
            errors.append("First name can only contain letters")
        if len(data['l_name']) < 2:
            errors.append("Last name must be at least 2 characters")
        if not data['l_name'].isalpha():
            errors.append("Last name can only contain letters")
        if len(data['email']) == 0:
            errors.append("Email is required")
        try:
            validate_email(data['email'])
        except ValidationError:
            errors.append("Invalid email")
        else:
            pass
        if len(data['password']) < 8:
            errors.append("Password must be at least 8 characters")
        if data['password'] != data['confirm']:
            errors.append("Passwords do not match")
        if len(errors) == 0:
            user = User.objects.create(f_name=data['f_name'],l_name=data['l_name'],email=data['email'],password=data['password'])
            return {'user': user, 'errors': None}
        else:
            return {'user': None, 'errors': errors}

    def login(self, data):
        errors = []
        try:
            user = User.objects.get(email = data['email'])
            if user.password != data['password']:
                errors.append("Incorrect password")
        except:
            errors.append('Incorrect Email')
        if len(errors) == 0:
            return {'user': user, 'errors': None}
        else:
            return {'user': None, 'errors': errors}

class User(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
