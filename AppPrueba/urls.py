from django.urls import path
from .views import *


urlpatterns = [
    
    path("empleados/", empleados, name= "empleados"),
    path("gerentes/", gerentes, name="gerentes"),
    path("encargados/", encargados, name="encargados"),
    path("", inicio, name="inicio"),

    
]   