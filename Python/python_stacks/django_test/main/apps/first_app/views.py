from django.shortcuts import render
def index(request):
    print ('*'*100)
    return render(request, 'first_app/index.html')

def show(request):
    print (request.method)
    return render(request, 'first_app/show_users.html')

# Create your views here.
