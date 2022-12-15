from django.urls import path
from .views import *


urlpatterns = [
    path('curso/', curso),
    path("cursos/", cursos),
    path("estudiantes/", estudiantes),
    path("profesores/", profesores),
    path("entregables/", entregables),
    path("", inicio),

    
]   