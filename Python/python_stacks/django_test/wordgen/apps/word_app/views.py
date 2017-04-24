from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
import string, random
import string
import random


def index(request):
    if 'attempt' in request.session:
        request.session['attempt'] += 1
    else:
        request.session['attempt'] = 1
    word = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(14))
    return render(request, 'word_app/index.html', {'word': word})
