# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from core.models import UsuarioModelo
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class DatosPersonales(UsuarioModelo):
	carrera = models.CharField(max_length=50)
	numero_control= models.CharField(max_length=50)
#	for num in range(1,13):
#		semestre_opc.append(num)
	semestre= models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(12)])
#	semestre_opc=(
#		('1',"1"),
#		('2',"2"),
#		('3',"3"),
#		('4',"4"),
#		('5',"5"),
#		('6',"6"),
#		('7',"7"),
#		('8',"8"),
#		('9',"9"),
#		('10',"10"),
#		('11',"11"),
#		('12',"12"),
#		)
#	semestre = models.CharField(choices=semestre_opc, max_length=50, default="1")
    ##la fecha creada esta en el usuario en create
class DatosGenerales(UsuarioModelo):
	apellido_paterno = models.CharField(max_length=50)
	apellido_materno= models.CharField(max_length=50)
	nombre = models.CharField( max_length=50)
	sexo_opc=(
		('m',"Masculino"),
		('f',"Femenino"),
		)
	sexo = models.CharField(choices=sexo_opc,max_length=50,blank=False)
	correo = models.EmailField()

	telefono =models.CharField( max_length=50,null=True)
	
	celular = models.CharField( max_length=50,null=True)

	fecha_nacimiento = models.DateField(null=False)
	
	lugar_nacimiento = models.CharField(max_length=50)

	estado_civil_opc=(
		('soltero',"Soltero"),
		('casado',"Casado"),
		('otro',"Otro")
		)
	estado_civil=models.CharField(choices=estado_civil_opc,
			default='soltero', max_length=50)

	numero_hijos = models.IntegerField(null=True)

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
		('bachillerato',"Esfuerzo de Bachillerato"),
		)
	becado_lugar=models.CharField(choices=becado_lugar_opc,
			default='federal', max_length=50,blank=True,null=True)

	becado_institucion = models.CharField(max_length=50,default="",blank=True)

	con_quien_vives_opc= (
		('familia',"Familia"),
		('familia_cercana',"Familia Cercana"),
		('estudiantes',"Estudiantes"),
		('solo',"Solo"),
		('otros',"Otros")
		)
	con_quien_vives=models.CharField(choices=con_quien_vives_opc,
			default='familia', max_length=50)

	trabajas_opc=(
		('si',"Sí"),
		('no',"No"),
		)
	trabajas =models.CharField(choices=trabajas_opc,
			default='no', max_length=50)

	trabajas_donde = models.CharField(max_length=50,default="",null=True,blank=True)
	trabajas_horario_inicio = models.TimeField(blank=True,null=True)
	trabajas_horario_salida = models.TimeField(blank=True,null=True)

	escolaridad_padre_opc = (
		('primaria',"Primaria"),
		('secundaria',"Secundaria"),
		('preparatoria',"Preparatoria"),
		('tecnico',"Técnico"),
		('lic',"Licenciatura"),
		('posgrado ',"Posgrado"),
		('sinestudio',"Sin estudio")
		)
	escolaridad_padre=models.CharField(choices=escolaridad_padre_opc,
			default='sinestudio', max_length=50,blank=True,null=True)


	escolaridad_madre_opc = (
		('primaria',"Primaria"),
		('secundaria',"Secundaria"),
		('preparatoria',"Preparatoria"),
		('tecnico',"Técnico"),
		('lic',"Licenciatura"),
		('posgrado ',"Posgrado"),
		('sinestudio',"Sin estudio")
		)
	escolaridad_madre=models.CharField(choices=escolaridad_madre_opc,
			default='sinestudio', max_length=50,blank=True,null=True)

	padre_vive_opc=(
		('si',"Vive"),
		('no',"Finado"),
		)
	padre_vive=models.CharField(choices=padre_vive_opc,
			default='si', max_length=50)

	madre_vive_opc=(
		('si',"Vive"),
		('no',"Finado"),
		)
	madre_vive=models.CharField(choices=madre_vive_opc,
			default='si', max_length=50)

	nom_trabajo_padre = models.CharField(max_length=50,default="",blank=True,null=True)
	nom_trabajo_madre = models.CharField(max_length=50,default="",blank=True,null=True)
	#ContactosEmergencia= JSONField(default={})
	Contacto_de_Emergencia_nombre = models.CharField(max_length=50)
	Contacto_de_Emergencia_numero= models.CharField(max_length=50)
#class ContactosEmergencia (models.Model):
#	usuario = models.OneToOneField(User,blank=True, null= True, on_delete=models.CASCADE)
#	nombre = models.CharField(max_length=50)
#	telefono = models.IntegerField()





# python manager.py makemigrations
# python manager.py migrate anexo6 
#python manager.py runserver