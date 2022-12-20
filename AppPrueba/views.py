from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.


def empleados(request):
    return render(request, "AppPrueba/empleados.html")

def gerentes(request):
    return render(request, "AppPrueba/gerentes.html")

def encargados(request):
    return render(request, "AppPrueba/encargados.html")

def inicio(request):
    return render(request, "AppPrueba/inicio.html")

