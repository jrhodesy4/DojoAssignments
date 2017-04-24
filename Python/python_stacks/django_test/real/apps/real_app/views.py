from django.shortcuts import render

def index(request):
    return render(request, 'real_app/index.html')

def about(request):
    return render(request, 'real_app/about.html')

def projects(request):
    return render(request, 'real_app/projects.html')

def testimonials(request):
    return render(request, 'real_app/testimonials.html')

# Create your views here.
