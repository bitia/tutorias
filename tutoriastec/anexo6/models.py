# -*- coding: utf-8 -*-
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

	estado_civil_opc=(
		('soltero',"Soltero"),
		('casado',"Casado"),
		)
	estado_civil=models.CharField(choices=estado_civil_opc,
			default='soltero', max_length=50)

	domicilio_actual = models.CharField(max_length=50,default="") 

	escolaridad_opc=(
		('preparatoria',"Preparatoria"),
		('bachillerato_tec',"Bachillerato Técnico"),
		)
	escolaridad=models.CharField(choices=escolaridad_opc,
			default='preparatoria', max_length=50)

	nombre_institucion = models.CharField(max_length=50,default="")

	becado_opc=(
		('si',"Sí"),
		('no',"No"),
		)
	becado=models.CharField(choices=becado_opc,
			default='no', max_length=50)

	becado_lugar_opc = (
		('federal',"Gobierno Federal"),
		('estatal',"Gobierno Estatal"),
		('bachillerato',"Esfuerzo de bachillerato"),
		)
	becado_lugar=models.CharField(choices=becado_lugar_opc,
			default='federal', max_length=50,blank=True)

	conquien_vives_opc= (
		('familia',"Familia"),
		('faminia_cercana',"Familia Cercana"),
		('estudiantes',"Estudiantes"),
		('solo',"Solo")
		)
	conquien_vives=models.CharField(choices=conquien_vives_opc,
			default='familia', max_length=50)

	trabajas_opc=(
		('si',"Sí"),
		('no',"No"),
		)
	trabajas =models.CharField(choices=trabajas_opc,
			default='no', max_length=50)

	trabajas_donde = models.CharField(max_length=50,default="")
	trabajas_horario_inicio = models.TimeField(null=True)
	trabajas_horario_salida = models.TimeField(null=True)
#	escolaridad_padre
#	escolaridad_madre
#	padre_vive
#	madre_vive
	nom_trabajo_padre = models.CharField(max_length=50,default="")
	nom_trabajo_madre = models.CharField(max_length=50,default="")


class ContactosEmergencia (models.Model):
	nombre = models.CharField(max_length=50)
	telefono = models.IntegerField()
	alumno = models.ForeignKey(DatosGenerales)





# python manager.py makemigrations
# python manager.py migrate anexo6 
#python manager.py runserver