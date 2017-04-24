from django.shortcuts import render, HttpResponse
import datetime
from django.utils.timezone import utc


def index(request):
    myDate = datetime.datetime.utcnow().replace(tzinfo=utc)
    # myDate = datetime.datetime.now()
    return render(request, 'time_app/index.html', {'myDate': myDate})

# Create your views here.
