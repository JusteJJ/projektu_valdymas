from django.shortcuts import render, HttpResponse
from .models import Projektas, Klientas, Darbuotojas, Darbas, Saskaita
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

@csrf_protect
def register(request):
    if request.method == "POST":
        pass
    return render(request, 'registration/register.html')

def login(request):
    if request.method == "POST":
        pass
    return render(request, 'accounts/login.html')

# Create your views here.
def index(request):
    kontekstas = {
        'vykdomi_projektai' : Projektas.objects.all()
    }
    return render(request, 'index.html', context=kontekstas)

def projektas(request):
    kontekstas = {
        'projektas': Projektas.objects.all()
    }
    return render(request, 'projektai.html', context=kontekstas)

def klientas1(request):
    kontekstas = {
        'klientas': Klientas.objects.all()
     }
    return render(request, 'projektai.html', context=kontekstas)

def Darbuotojas(request):
     kontekstas = {
         'darbuotojas': Darbuotojas().objects.all()
     }
     return render(request, 'projektai.html', context=kontekstas)

def Darbas(request):
     kontekstas = {
         'darbas': Darbas().objects
     }
     return render(request, 'projektai.html', context=kontekstas)

def Saskaita(request):
     kontekstas = {
         'saskaita': Saskaita().objects.all
     }
     return render(request, 'projektai.html', context=kontekstas)
