from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse("Holi, estas en la url / ")

def equipolau(request):
    # context = {"equipo": "LA U"}, 
    return render(request, 'infogol/infogol.html')
    
