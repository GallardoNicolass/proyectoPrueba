from django import forms 

class EmpleadoForm(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=50)
    apellido= forms.CharField(label="Apellido", max_length=50)
    legajo= forms.IntegerField(label="legajo")


class GerenteForm(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=50)
    apellido= forms.CharField(label="Apellido", max_length=50)
    legajo= forms.IntegerField(label="legajo")
    


class EncargadoForm(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=50)
    apellido= forms.CharField(label="Apellido", max_length=50)
    sucursal= forms.IntegerField(label="sucursal")
