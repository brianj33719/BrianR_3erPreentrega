from django import forms

class Alojamientosform(forms.Form):
    hotel = forms.CharField(max_length=50, required=True, label="Nombre del Hotel")
    categoriaEstrellas = forms.IntegerField(required=True, label="Categoría en Estrellas")
    
class Paquetesform(forms.Form):
    hotel = forms.CharField(max_length=50, required=True, label="Nombre del Hotel")
    nombreAerolinea = forms.CharField(max_length=50, required=True, label="Nombre de la Aerolínea")
    estadiaNoches = forms.IntegerField(required=True, label="Estadía en noches")
    
class Vuelosform(forms.Form):
    nombreAerolinea = forms.CharField(max_length=50, required=True, label="Nombre de la Aerolínea")
