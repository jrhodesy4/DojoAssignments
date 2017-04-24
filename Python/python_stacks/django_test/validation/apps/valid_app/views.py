from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, "valid_app/index.html")

def valid(request):
    if request.method =="POST":
        data_stuff = {
        'name' : request.POST['name']
        }
        result = User.objects.validate(data_stuff)
        if result['errors'] == None:
            request.session['name'] = result['user'].name
            request.session['user'] = result['user'].id
            return redirect('/results')
        else:
            for error in result['errors']:
                messages.add_message(request, messages.ERROR, error)
            return redirect('/')

def results(request):
    all_users = User.objects.all()
    new_username = request.session['name']
    return render(request, 'valid_app/success.html', {'all_users': all_users, 'new_username': new_username})

def regress(request):
    return redirect('/')
