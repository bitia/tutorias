from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DatosPersonales(models.Model):
	carrera = models.CharField(max_length=30)
	numero_control = models.IntegerField()
	semestre = models.IntegerField()
	fecha = models.DateField()
	
class DatosGenerales(models.Model):
	apellido_paterno = models.CharField(max_length=50)
	apellido_materno= models.CharField(max_length=50)
	nombre = models.CharField( max_length=50)
	sexo = models.CharField(max_length=50)
	correo = models.EmailField()
	telefono = models.IntegerField()
	celular = models.IntegerField()
	fecha_nacimiento = models.DateField()
	lugar_nacimiento = models.CharField(max_length=50)
	estado_civil = models.CharField(max_length=50)