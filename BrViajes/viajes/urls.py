from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('alojamientos/', alojamientos, name="alojamientos"),
    path('paquetes/', paquetes, name="paquetes"),
    path('vuelos/', vuelos, name="vuelos"),
    
    path('acerca/', acerca, name="acerca"),
    
    path('alojamientosForm/', alojamientosform, name="alojamientosForm"),
    path('paquetesForm/', paquetesform, name="paquetesForm"),
    path('vuelosForm/', vuelosform, name="vuelosForm"),
    path('buscarAlojamientos/', buscarAlojamientos, name="buscarAlojamientos"),
    path('encontrarAlojamientos/', encontrarAlojamientos, name="encontrarAlojamientos"),
]