from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import bcrypt

class UserManager(models.Manager):
    def register(self,data):
        errors = []
        if len(data['name']) < 2:
            errors.append("Name must be at least 2 characters")
        if not data['name'].isalpha():
            errors.append("Name can only contain letters")
        if len(data['alias']) < 2:
            errors.append("Alias must be at least 2 characters")
        if not data['alias'].isalpha():
            errors.append("Alias can only contain letters")
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
            data['password'] = bcrypt.hashpw(data['password'].encode('utf8'), bcrypt.gensalt())
            user = User.objects.create(name=data['name'],alias=data['alias'],email=data['email'],password=data['password'])
            return {'user': user, 'errors': None}
        else:
            return {'user': None, 'errors': errors}

    def login(self, data):
        errors = []
        try:
            user = User.objects.get(email = data['email'])
            if bcrypt.hashpw(data['password'].encode('utf8'), user.password.encode('utf8')) == user.password.encode('utf8'):
                print 'success'
        except:
            errors.append('Incorrect Email')
        if len(errors) == 0:
            return {'user': user, 'errors': None}
        else:
            return {'user': None, 'errors': errors}

class BooksManager(models.Manager):
    def create_book(self, data):
        errors = []
        if len(data['title']) == 0:
            errors.append("Title cannot be blank")




class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Author(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Books(models.Model):
    author_id = models.ForeignKey(Author, related_name='authors', default=1)
    user = models.ForeignKey(User, related_name='users')
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reviews(models.Model):
    user_id = models.ForeignKey(User, related_name='reviews')
    book_id = models.ForeignKey(Books, related_name='reviews', blank=True, null=True)
    content = models.TextField()
    rating = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
