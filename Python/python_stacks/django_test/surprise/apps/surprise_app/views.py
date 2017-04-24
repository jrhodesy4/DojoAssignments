from django.shortcuts import render, redirect
import random
VALUES = ['hey', 'hi', 'hello', 'howdy', 'aloha', 'hola']

def index(request):
    return render(request, 'surprise_app/index.html')

def result(request):
    if request.method == "POST":
        result = random.sample((VALUES),int(request.POST['number']))
        print result[1]
        return render(request, 'surprise_app/result.html', {'result': result})
    else:
        return redirect('/')

# Create your views here.
