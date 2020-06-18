from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    return HttpResponse("Holi, estas en la url / ")

@login_required
def equipolau(request):
    # context = {"equipo": "LA U"}, 
    return render(request, 'infogol/info_forofo.html')
    
