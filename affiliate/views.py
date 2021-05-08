from django.http.request import HttpRequest
from django.shortcuts import render
from .models import Boxer
from django.http import HttpResponse

# Create your views here.
def home(request):
    boxers = Boxer.objects.all()
    # output = '. '.join([l.last_name for l in boxers])
    # return HttpResponse(output)
    return render(request, 'home.html', {'boxer': boxers})

def contact(request):
    return render(request, 'contact.html', {})


