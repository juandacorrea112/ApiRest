from django.db import models

class Tutorial(models.Model):
    Tatuador = models.CharField(max_length=100, blank=False, default='')
    Fecha = models.DateField()
    Hora = models.TimeField()
    Imagen = models.ImageField()
    Descripcion = models.CharField(max_length=250, blank=False, default='')