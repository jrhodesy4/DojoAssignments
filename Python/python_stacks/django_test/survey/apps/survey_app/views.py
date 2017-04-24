from django.shortcuts import render, redirect

def index(request):
    return render(request, 'survey_app/index.html')

def submit(request):
    if 'id' in request.session:
        request.session['id'] += 1
    else:
        request.session['id'] = 1
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['dojo']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']
        return redirect('/results')
    else:
        return redirect('/results')

def results(request):
    return render(request, 'survey_app/results.html')

def regress(request):
    return redirect('/')


# Create your views here.
