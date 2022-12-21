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
    

    
]   