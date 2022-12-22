from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppPrueba.forms import EmpleadoForm, GerenteForm, EncargadoForm

# Create your views here.


def empleados(request):
    return render(request, "AppPrueba/empleados.html")

def gerentes(request):
    return render(request, "AppPrueba/gerentes.html")

def encargados(request):
    return render(request, "AppPrueba/encargados.html")

def inicio(request):
    return render(request, "AppPrueba/inicio.html")

"""def empleadoFormulario(request):
    if request.method=="POST":
        nombre= request.POST["nombre"]
        apellido= request.POST["apellido"]
        legajo= request.POST["legajo"]
        empleado= Empleado(nombre=nombre, apellido=apellido, legajo=legajo)
        empleado.save()
        return render(request, "AppPrueba/inicio.html",{"mensaje": "Empleado guardado correctamente"})
        
    else:
        return render (request, "AppPrueba/empleadoFormulario.html")""" 


def empleadoFormulario(request):
    if request.method=="POST":
        form= EmpleadoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre= informacion["nombre"]
            apellido= informacion["apellido"]
            legajo= informacion["legajo"]
            empleado= Empleado(nombre=nombre, apellido=apellido, legajo=legajo)
            empleado.save()
            return render(request, "AppPrueba/inicio.html", {"mensaje": "Emplado guardado correctamente"})
        else:
            return render(request, "AppPrueba/empleadoFormulario.html" ,{"form": form, "mensaje": "informacion no valida"})

    else:
        formulario= EmpleadoForm()
        return render (request, "AppPrueba/empleadoFormulario.html", {"form": formulario})




def gerenteFormulario(request):
    if request.method=="POST":
        form= GerenteForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre= informacion["nombre"]
            apellido= informacion["apellido"]
            legajo= informacion["legajo"]
            gerente= Gerente(nombre=nombre, apellido=apellido, legajo=legajo)
            gerente.save()
            return render(request, "AppPrueba/inicio.html", {"mensaje": "Gerente guardado correctamente"})
        else:
            return render(request, "AppPrueba/gerenteFormulario.html" ,{"form": form, "mensaje": "informacion no valida"})

    else:
        formulario= GerenteForm()
        return render (request, "AppPrueba/gerenteFormulario.html", {"form": formulario})



def encargadoFormulario(request):
    if request.method=="POST":
        form= EncargadoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre= informacion["nombre"]
            apellido= informacion["apellido"]
            sucursal= informacion["sucursal"]
            encargado= Encargado(nombre=nombre, apellido=apellido, sucursal=sucursal)
            encargado.save()
            return render(request, "AppPrueba/inicio.html", {"mensaje": "Encargado guardado correctamente"})
        else:
            return render(request, "AppPrueba/encargadoFormulario.html" ,{"form": form, "mensaje": "informacion no valida"})

    else:
        formulario= EncargadoForm()
        return render (request, "AppPrueba/encargadoFormulario.html", {"form": formulario})




def busquedaLegajo(request):
    return render(request, "AppPrueba/busquedaLegajo.html")


def buscar(request):

    legajo= request.GET["legajo"]
    if legajo!="":

        empleados= Empleado.objects.filter(legajo__icontains=legajo)
        return render(request, "AppPrueba/resultadosBusqueda.html", {"empleados": empleados})
    else:
        return render(request, "AppPrueba/busquedaLegajo.html", {"mensaje": "Che ingresa una comision para buscar"})

    


