from django.shortcuts import render, redirect
from .models import Courses

def index(request):
    context = {
    'courses' : Courses.objects.all()
    }
    return render(request, "courses_app/index.html", context)

def delete(request, id):
    course_id=request.session['id']
    context = {
    'courses' : Courses.objects.filter(id = course_id)
    }
    return render(request, 'courses_app/delete.html', conte)

def submit(request):
    Courses.objects.create(name=request.POST['name'],description=request.POST['description'])
    return redirect('/')

def destroy(request):
    course_id = request.session['id']

    if request.method == 'POST':
        if request.POST['delete'] == 'no':
            return redirect('/')
        if request.POST['delete'] == 'yes':
            Courses.objects.filter(id = course_id).delete()
            return redirect('/')



# Create your views here.
