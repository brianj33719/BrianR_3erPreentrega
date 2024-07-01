from django.shortcuts import render
from .models import *

from .forms import *
 
def home(request):
    return render(request, "viajes/index.html")

def alojamientos(request):
    contexto = {"alojamientos": Alojamientos.objects.all()}
    return render(request, "viajes/alojamientos.html", contexto)

def vuelos(request):
    contexto = {"vuelos": Vuelos.objects.all()}
    return render(request, "viajes/vuelos.html", contexto)

def paquetes(request):
    contexto = {"paquetes": Paquetes.objects.all()}
    return render(request, "viajes/paquetes.html", contexto)

def acerca(request):
    return render(request, "viajes/acerca.html")

def alojamientosform(request):
    if request.method == "POST":
        miForm = Alojamientosform(request.POST)
        if miForm.is_valid():
            alojamientos_hotel = miForm.cleaned_data.get("hotel")
            alojamientos_estrellas = miForm.cleaned_data.get("categoriaEstrellas")
            alojamientos = Alojamientos(hotel=alojamientos_hotel, categoriaEstrellas=alojamientos_estrellas)
            alojamientos.save()
            contexto = {"alojamientos": Alojamientos.objects.all()}
            return render(request, "viajes/alojamientos.html", contexto) 
    else:
        miForm = Alojamientosform()
         
    return render(request, "viajes/alojamientosForm.html", {"form": miForm})

def paquetesform(request):
    if request.method == "POST":
        miForm = Paquetesform(request.POST)
        if miForm.is_valid():
            paquetes_hotel = miForm.cleaned_data.get("hotel")
            paquetes_nombreAerolinea = miForm.cleaned_data.get("nombreAerolinea")
            paquetes_estadiaNoches = miForm.cleaned_data.get("estadiaNoches")
            paquetes = Paquetes(hotel=paquetes_hotel, nombreAerolinea=paquetes_nombreAerolinea, estadiaNoches=paquetes_estadiaNoches)
            paquetes.save()
            contexto = {"paquetes": Paquetes.objects.all()}
            return render(request, "viajes/paquetes.html", contexto) 
    else:
        miForm = Paquetesform()
         
    return render(request, "viajes/paquetesForm.html", {"form": miForm})

def vuelosform(request):
    if request.method == "POST":
        miForm = Vuelosform(request.POST)
        if miForm.is_valid():
            vuelos_Aerolinea = miForm.cleaned_data.get("nombreAerolinea")
            vuelos = Vuelos(nombreAerolinea=vuelos_Aerolinea)
            vuelos.save()
            contexto = {"vuelos": Vuelos.objects.all()}
            return render(request, "viajes/vuelos.html", contexto) 
    else:
        miForm = Vuelosform()
         
    return render(request, "viajes/vuelosForm.html", {"form": miForm})

def buscarAlojamientos(request):
    return render(request, "viajes/buscar.html" )

def encontrarAlojamientos(request):
    if request.GET["buscar"]:
        metodo = request.GET["buscar"]
        alojamientos = Alojamientos.objects.filter(hotel__icontains=metodo)
        contexto = {"alojamientos": alojamientos}
    else:
        contexto = {"alojamientos": Alojamientos.objects.all()}
        
    return render(request, "viajes/alojamientos.html", contexto)