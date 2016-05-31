from __future__ import unicode_literals

from django.db import models

# Create your models here.

class AnexoItem(models.Model):
    titulo = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50, blank=True)
    imagen = models.ImageField(blank=True)
    num_formularios = models.IntegerField()
    
