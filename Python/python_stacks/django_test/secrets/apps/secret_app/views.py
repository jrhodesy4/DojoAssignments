from django.shortcuts import render, redirect
from .models import User, Secret, Likes
from django.contrib import messages
import bcrypt
from django.db.models import Count

def index(request):
	return render(request, "secret_app/index.html")

def register(request):
    if request.method =="POST":
        data_stuff = {
        'f_name' : request.POST['f_name'],
        'l_name' : request.POST['l_name'],
        'email' : request.POST['email'],
        'password' : request.POST['password'],
        'confirm' : request.POST['confirm']
        }
        result = User.objects.register(data_stuff)
        if result['errors'] == None:
            request.session['name'] = result['user'].f_name
            request.session['user'] = result['user'].id
            request.session['action'] = "registered"
            return redirect('/secrets')
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
            request.session['name'] = result['user'].f_name
            request.session['user'] = result['user'].id
            request.session['action'] = "logged in"
            return redirect('/secrets')
        else:
            for error in result['errors']:
                messages.add_message(request, messages.ERROR, error)
            return redirect('/')

def secrets(request):
    if 'user' not in request.session:
        return redirect('/')
    new_username = request.session['name']
    context = {
    'secrets' : Secret.objects.all().order_by('-created_at'),
    'new_username' : new_username
    }
    print request.session['user']
    return render(request, "secret_app/secrets.html", context)

def back(request):
    return redirect('/secrets')

def message(request):
    if request.method =="POST":
        message = Secret.objects.create(user_id = User.objects.get(id = request.session['user']), content = request.POST['content'])
    return redirect('/secrets')

def like(request, id, page):
    new_like, created = Likes.objects.get_or_create(secret= Secret.objects.get(id = id), user= User.objects.get(id = request.session['user']))
    if not created:
        return redirect('/'+page)
    else:
        return redirect('/'+page)

def popular(request):
    if 'user' not in request.session:

        return redirect('/')
    context = {
    'secrets' : Secret.objects.annotate(num_likes=Count('likes')).order_by('-num_likes'),
    }
    return render(request, "secret_app/popular.html", context)

def delete(request, id, page):
    destroy = Secret.objects.filter(id = id).delete()
    return redirect('/'+page)


def logout(request):
    request.session.clear()
    return redirect('/')
