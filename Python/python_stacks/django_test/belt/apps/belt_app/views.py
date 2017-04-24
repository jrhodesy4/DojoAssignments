from django.shortcuts import render, redirect
from .models import User, Reviews, Books, Author
from django.contrib import messages
import bcrypt
from django.db.models import Count
from django.core.urlresolvers import reverse

def index(request):
	return render(request, "belt_app/index.html")

def register(request):
    if request.method =="POST":
        data_stuff = {
        'name' : request.POST['name'],
        'alias' : request.POST['alias'],
        'email' : request.POST['email'],
        'password' : request.POST['password'],
        'confirm' : request.POST['confirm']
        }
        result = User.objects.register(data_stuff)
        if result['errors'] == None:
            request.session['name'] = result['user'].name
            request.session['user'] = result['user'].id
            request.session['action'] = "registered"
            return redirect('/main')
        else:
            for error in result['errors']:
                messages.add_message(request, messages.ERROR, error)
            return redirect('/')

def login(request):
    if request.method =="POST":
        data_stuff = {
        'email' : request.POST['email'],
        'password' : request.POST['password']
        }
        result = User.objects.login(data_stuff)
        if result['errors'] == None:
            request.session['name'] = result['user'].name
            request.session['user'] = result['user'].id
            request.session['action'] = "logged in"
            return redirect('/main')
        else:
            for error in result['errors']:
                messages.add_message(request, messages.ERROR, error)
            return redirect('/')

def main(request):
    if 'user' not in request.session:
        return redirect('/')
    new_username = request.session['name']
    context = {
    'books' : Books.objects.all().order_by('-created_at'),
    'authors': Author.objects.all().order_by('-created_at'),
    'reviews' : Reviews.objects.all().order_by('-created_at'),
    'new_username' : new_username
    }
    return render(request, 'belt_app/main.html', context)

def message(request):
    if request.method =="POST":
        books = Books.objects.create(user = User.objects.get(id = request.session['user']), title = request.POST['title'], author_id = Author.objects.get(id = authors.id))
        author = Author.objects.create(name = request.POST['author'])
        review = Reviews.objects.create(user_id = User.objects.get(id = request.session['user']), book_id = Books.objects.get(id = books.id), content = request.POST['content'], rating=request.POST['stars'])
        request.session['id'] = books.id
        print books.id
        return redirect(reverse('my_book', kwargs={'id': books.id}))

def add(request):
    return render(request, 'belt_app/add.html')

def books(request, id):
    request.session['id'] = id
    print id
    context = {
    'reviews' : Reviews.objects.filter(id=id),
    'books': Books.objects.filter(id=id)
    }
    return render(request, 'belt_app/books.html', context)

def review(request):
    if request.method =="POST":
        review = Reviews.objects.create(user_id = User.objects.get(id = request.session['user']), book_id = Books.objects.get(id =request.session['id']), content = request.POST['content'])
        return redirect(reverse('my_book', kwargs={'id': books.id}))

def user_page(request, id):
    context = {
    'users' : User.objects.filter(id = id),
    }
    return render(request, 'belt_app/user.html', context)

def delete(request, id, page):
    destroy = Reviews.objects.filter(id = id).delete()
    return redirect('/'+page)

def logout(request):
    request.session.clear()
    return redirect('/')
