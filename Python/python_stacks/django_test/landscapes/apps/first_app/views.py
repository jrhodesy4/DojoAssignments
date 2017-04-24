from django.shortcuts import render, HttpResponse
def index(request):
    return render(request, 'first_app/index.html')

def number(request, num):
    if int(num) < 11:
        photo = "first_app/snow.jpg"
    elif int(num) < 21:
        photo = "first_app/desert.jpg"
    elif int(num) < 31:
        photo = "first_app/forest.jpg"
    elif int(num) < 41:
        photo = "first_app/vineyard.png"
    elif int(num) < 51:
        photo = "first_app/tropical.jpg"
    return render(request, 'first_app/pics.html', {'photo': photo})
# Create your views here.
