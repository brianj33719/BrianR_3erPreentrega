from django.db import models

# Modelos de mi aplicación de viajes:

class Alojamientos(models.Model):
    hotel = models.CharField(max_length=50)
    categoriaEstrellas = models.IntegerField()
    
    class Meta:
        verbose_name = "Alojamiento"
        verbose_name_plural = "Alojamientos"
        ordering = [ "-categoriaEstrellas" ] 
    def __str__(self):
        return f"{self.hotel}"
    
class Vuelos(models.Model):
    nombreAerolinea = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Vuelo"
        verbose_name_plural = "Vuelos"
    
    def __str__(self):
        return f"{self.nombreAerolinea}"
    
class Paquetes(models.Model):
    hotel = models.CharField(max_length=50)
    nombreAerolinea = models.CharField(max_length=50)
    estadiaNoches = models.IntegerField()
    
    class Meta:
        verbose_name = "Paquete"
        verbose_name_plural = "Paquetes"
    
    def __str__(self):
        return f"{self.hotel}, {self.nombreAerolinea}"
