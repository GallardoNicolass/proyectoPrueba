from django.shortcuts import render
from .models import Curso, Profesor
from django.http import HttpResponse

# Create your views here.


def curso(request):

    curso= Curso(nombre="JavaScript", comision=123456)
    curso.save()
    cadena_texto=f"curso guardado: Nombre: {curso.nombre}, comision: {curso.comision}"
    return HttpResponse(cadena_texto)

