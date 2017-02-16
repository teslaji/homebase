from django.shortcuts import render
#from django.http import Http404
#from django.template import loader
from django.http import HttpResponse

def home (request):
        return render(request, "main/home.html",{'message':'Companies House UK'})
