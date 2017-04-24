from django.shortcuts import render, redirect, HttpResponse
import datetime
from django.utils.timezone import utc
import random

def index(request):
    if 'totalgold' not in request.session:
        request.session['totalgold'] = 0
    return render(request, 'nin_gold/index.html')

def goldilocks(request):
    myDate = datetime.datetime.utcnow().strftime('%y/%m/%d %H:%M %p')
    if request.method == "POST":
        if 'log' not in request.session:
            request.session['log'] = ''
        farmgold = random.randrange(10,21)
        cavegold = random.randrange(5,11)
        housegold = random.randrange(2,6)
        casinogold = random.randrange(0,51)
        if request.POST['building'] == 'farm':
            request.session['totalgold'] += farmgold
            request.session['log'] += '<p class="win">You won ' + str(farmgold) + ' golds at the ' + request.POST['building'] + ' ' + '(' + str(myDate) + ')</p>'

        elif request.POST['building'] == 'cave':
            request.session['totalgold'] += cavegold
            request.session['log'] += '<p class="win">You won ' + str(cavegold) + ' golds at the ' + request.POST['building'] + ' ' + '(' + str(myDate) + ')</p>'

        elif request.POST['building'] == 'house':
            request.session['totalgold'] += housegold
            request.session['log'] += '<p class="win">You won ' + str(housegold) + ' golds at the ' + request.POST['building'] + ' ' + '(' + str(myDate) + ')</p>'

        elif request.POST['building'] == 'casino':
            result = random.randint(0, 1)
            if result == 0:
                request.session['totalgold'] -= casinogold
                request.session['response'] = 'Loser'
                request.session['log'] += '<p class="lose">You lost ' + str(casinogold) + ' at the ' + request.POST['building'] + ' ' + '(' + str(myDate) + ')</p>'
                print request.session['log']
            else:
                request.session['totalgold'] += casinogold
                request.session['response'] = 'Winner'
                request.session['log'] += '<p class="win">You won ' + str(casinogold) + ' golds at the ' + request.POST['building'] + ' ' + '(' + str(myDate) + ')</p>'
        return redirect('/')
    else:
        return redirect('/')

def reset(request):
    if request.method == "POST":
        request.session['totalgold'] = 0
        request.session['log'] = ''
        return redirect('/')
    else:
        return redirect('/')


# Create your views here.
