from django.contrib import admin
from .models import Empleado, Encargado, Gerente


admin.site.register(Empleado)
admin.site.register(Encargado)
admin.site.register(Gerente)