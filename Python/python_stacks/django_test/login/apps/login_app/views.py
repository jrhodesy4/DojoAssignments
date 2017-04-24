from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
	return render(request, "login_app/index.html")

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
            return redirect('/success')
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
            return redirect('/success')
        else:
            for error in result['errors']:
                messages.add_message(request, messages.ERROR, error)
            return redirect('/')

def success(request):
    new_username = request.session['name']
    return render(request, "login_app/success.html", {'new_username': new_username})

def logout(request):
    return redirect('/')
