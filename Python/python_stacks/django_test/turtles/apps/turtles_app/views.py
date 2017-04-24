from django.shortcuts import render, HttpResponse

def index(request):
    hello = 'No ninjas here'
    return HttpResponse(hello)

def all(request):
    return render(request, 'turtles_app/all.html')

def one(request, color):
    if color == 'blue':
        pic = "turtles_app/leonardo.jpg"
    elif color == 'orange':
        pic = "turtles_app/michelangelo.jpg"
    elif color == 'red':
        pic = "turtles_app/raphael.jpg"
    elif color == 'purple':
        pic = "turtles_app/donatello.jpg"
    else:
        pic = "turtles_app/notapril.jpg"
    return render(request, 'turtles_app/one.html', {'pic': pic})


# Create your views here.
