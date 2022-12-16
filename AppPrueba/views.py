from django.shortcuts import render
from .models import Curso, Profesor
from django.http import HttpResponse

# Create your views here.


def curso(request):

    curso= Curso(nombre="JavaScript", comision=34645)
    curso.save()
    cadena_texto=f"curso guardado: Nombre: {curso.nombre}, comision: {curso.comision}"
    return HttpResponse(cadena_texto)

def cursos(request):
    return render(request, "AppPrueba/cursos.html")

def estudiantes(request):
    return render(request, "AppPrueba/estudiantes.html")

def profesores(request):
    return render(request, "AppPrueba/profesores.html")

def entregables(request):
    return render(request, "AppPrueba/entregables.html")

def inicio(request):
    return render(request, "AppPrueba/inicio.html")

