from django.urls import path
from .views import *


urlpatterns = [
    
    path("empleados/", empleados, name= "empleados"),
    path("gerentes/", gerentes, name="gerentes"),
    path("encargados/", encargados, name="encargados"),
    path("", inicio, name="inicio"),
    path("empleadoFormulario/", empleadoFormulario, name="empleadoFormulario"),
    path("gerenteFormulario/", gerenteFormulario, name="gerenteFormulario"),
    path("encargadoFormulario/", encargadoFormulario, name="encargadoFormulario"),
    path("busquedaLegajo/", busquedaLegajo, name="busquedaLegajo"),
    path("buscar/", buscar, name="buscar"),
    path("leerEmpleados/", leerEmpleados, name="leerEmpleados"),
    path("elminarEmpleado/<id>", eliminarEmpleado, name="eliminarEmpleado"),
    path("editarEmpleado/<id>", editarEmpleado, name="editarEmpleado"),
    

    
]   