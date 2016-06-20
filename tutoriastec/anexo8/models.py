# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from core.models import UsuarioModelo ,TiempoModelo
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class FormatoEntrevista(UsuarioModelo):
	
	#nombre anexo6/models.py/Datosgenerales
	estatura = models.FloatField()
	peso = models.FloatField()
	carrera = models.CharField(max_length=50)
	#fecha nacimiento anexo6/models.py/Datosgenerales
	#sexo anexo6/models.py/Datosgenerales
	#edad anexo6/models.py/Datosgenerales
	codigo_postal = models.IntegerField()

	tipo_vivienda_opc=(
		('casa',"Casa"),
		('departamento',"Departamento"),
		)
	tipo_vivienda=models.CharField(choices=tipo_vivienda_opc,
			default='casa', max_length=50)
	estadovivienda_opc=(
		('propia',"Propia"),
		('rentada',"Rentada"),
		('prestada',"Prestada"),
		('otro',"Otro"),
		)
	estadovivienda =models.CharField(choices=estadovivienda_opc,default ='propia',max_length=100)
	especificacion_vivienda = models.CharField(max_length=50,default="")
	personas_vives = models.IntegerField()

	nom_padre = models.CharField(max_length=50)
	edad_padre = models.IntegerField()

	opc_si_no=(
		('si',"Si"),
		('no',"No"),
		)
	padre_trabaja=models.CharField(choices=opc_si_no,
			default='si', max_length=50)
	
	padre_profesion = models.CharField(max_length=50)
	padre_tipo_trabajo = models.CharField(max_length=50)
	padre_domicilio = models.CharField(max_length=50)
	padre_telefono = models.IntegerField()

	nom_madre = models.CharField(max_length=50)
	edad_madre = models.IntegerField()

	
	madre_trabaja=models.CharField(choices=opc_si_no,
			default='si', max_length=50)
	
	madre_profesion = models.CharField(max_length=50)
	madre_tipo_trabajo = models.CharField(max_length=50)
	madre_domicilio = models.CharField(max_length=50)
	madre_telefono = models.IntegerField()
	ingresos_mensuales_f = models.FloatField()
	ingresos_mensuales_p = models.FloatField()
	donde_primaria = models.CharField(max_length=50)
	donde_secundaria = models.CharField(max_length=50)
	donde_bachillerato = models.CharField(max_length=50)
	donde_estud_superiores = models.CharField(max_length=50)

	prescripcion_medica=models.CharField(choices=opc_si_no,
			default='no', max_length=50)

	prescripcion_medica_cuales_opc=(
		('vista',"Vista"),
		('oido',"Oido"),
		('lenguaje',"Lenguaje"),
		('otro',"Otro"),
		)
	prescripcion_medica_cuales=models.CharField(choices=prescripcion_medica_cuales_opc,
			max_length=50)
	comentarios= JSONField(default={})


class EstadoPsicofisiologicos(UsuarioModelo):

		opc_123 =(
		('1',"Muy frecuente"),
		('2',"Frecuente"),
		('3',"A veces"),
		('4',"Antes"),
		('5',"Nunca"),
		)
		mop_hinchados=models.CharField(choices=opc_123,
			default='5', max_length=50)
		dolores_vientre=models.CharField(choices=opc_123,default="5",
			max_length=50)
		dolores_cabeza=models.CharField(choices=opc_123,default="5",
			max_length=50)
		perdidad_equilibrio=models.CharField(choices=opc_123,default="5",
			max_length=50)
		fatiga=models.CharField(choices=opc_123,default="5",
			max_length=50)
		perdida_vista=models.CharField(choices=opc_123,default="5",
			max_length=50)
		dificultades_dormir=models.CharField(choices=opc_123,default="5",
			max_length=50)
		pesadillas=models.CharField(choices=opc_123,default="5",
			max_length=50)
		incontinencia=models.CharField(choices=opc_123,default="5",
			max_length=50)
		tartamudeo=models.CharField(choices=opc_123,default="5",
			max_length=50)
		observaciones_higiene = models.TextField()
		comentarios= JSONField(default={})
		

class DatosHermanos(TiempoModelo):
	usuario= models.ForeignKey(User,blank=True, null= True)
	nombre = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField()
	
	sexo_opc=(
		('m',"Masculino"),
		('f',"Femenino"),
		)
	sexo=models.CharField(choices=sexo_opc,blank=False, max_length=50)

	estudios_opc = (
		('primaria',"Primaria"),
		('secundaria',"Secundaria"),
		('preparatoria',"Preparatoria"),
		('tecnico',"Tecnico"),
		('lic',"Lic"),
		('posgrado ',"Posgrado"),
		('sinestudio',"Sin estudio")
		)
	estudios=models.CharField(choices=estudios_opc,
			max_length=50)
	relacion_opc = (
		('1',"Muy buena"),
		('2',"Buena"),
		('3',"Regular"),
		('4',"Mala"),
		('5',"Muy mala"),
		)
	relacion_con_hermano=models.CharField(choices=relacion_opc,
			default='2',max_length=50)

	actitud_con_hermano=models.CharField(choices=relacion_opc,
			default='2',max_length=50)

	
class AreaIntegracion(UsuarioModelo):
	
	relacion_opc = (
		('1',"Muy buena"),
		('2',"Buena"),
		('3',"Regular"),
		('4',"Mala"),
		('5',"Muy mala"),
		)
	relacion_familia=models.CharField(choices=relacion_opc,
			default='2',max_length=50)

	dificultades_fam_opc = (
		('si',"Si"),
		('no',"No"),
		)
	dificultades_fam=models.CharField(choices=dificultades_fam_opc,
			default='no',max_length=50)

	dificultades_fam_tipo = models.TextField(blank= True)
	
	actitud_con_familia=models.CharField(choices=relacion_opc,
			default='2',max_length=50)
	relacion_con_padre=models.CharField(choices=relacion_opc,
			default='2',max_length=50)
	actitud_con_padre=models.CharField(choices=relacion_opc,
			default='2',max_length=50)
	relacion_con_madre=models.CharField(choices=relacion_opc,
			default='2',max_length=50)
	actitud_con_madre=models.CharField(choices=relacion_opc,
			default='2',max_length=50)

	fam_opc = (
		('1',"Papá"),
		('2',"Mamá"),
		('3',"Hermano"),
		('4',"Hermana"),
		('5',"Tios"),
		)
	sientes_ligado = models.CharField(choices=fam_opc, max_length=50)	
	sientes_ligado_por = models.TextField(blank= True)
	ocupa_educacion = models.CharField(choices=fam_opc,max_length=50)
	influido_estudiar = models.CharField(choices=fam_opc,max_length=50)
	otro_inf_familiar = models.TextField(blank=True)
#  :::::::::::::::::::::::::::::::::::::::::::integracion social
	relacion_con_companeros=models.CharField(choices=relacion_opc,
			default='2',max_length=50)

	relacion_companeros_porque = models.TextField()
	relacion_con_amigos=models.CharField(choices=relacion_opc,
			default='2',max_length=50)

	relacion_companeros_porque = models.TextField(default="")
	pareja_opc = (
		('si',"Si"),
		('no',"No"),
		)
	pareja=models.CharField(choices=pareja_opc,
			default='no',max_length=50)
	relacion_pareja = models.CharField(choices=relacion_opc,
			default='2',max_length=50)
	relacion_profesores = models.CharField(choices=relacion_opc,
			default='2',max_length=50)
	relacion_autoridadesacademicas = models.CharField(choices=relacion_opc,
			default='2',max_length=50)

	tiempo_libre = models.CharField(max_length=50,default="")
	act_recreativa = models.CharField(max_length=50,default="")
	comentarios=JSONField(default={})

class CaracteristicasPersonales(UsuarioModelo):

	opc_caracteristicas = (
		('1',"No"),
		('2',"Poco"),
		('3',"Frecuente"),
		('4',"Mucho"),
		)
	puntual = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	timido = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	alegre = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	agresivo = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	abierto_ideas = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	reflexivo = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	constante = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	optimista = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	impulsivo = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	silencioso = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	generoso = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	inquieto = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	cambio_humor = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	dominante = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	egoista = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	sumiso = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	confiado_simismo = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	imaginativo = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	iniciativa = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	sociable = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	responsable = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	perseverante = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	motivado = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	activo = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	independiente = models.CharField(choices=opc_caracteristicas,
			default='1',max_length=50)
	comentarios=JSONField(default={})

	
class AreaPsicopedagogica(UsuarioModelo):
	
	gustaria_ser = models.CharField(max_length=50,blank=False)
	ayuda_casa_tareas = models.CharField(max_length=50,blank=False)
	problemas_intervienen = models.CharField(max_length=50,blank=False)
	rendimiento_escolar_opc = (
		('1',"Muy bueno"),
		('2',"Bueno"),
		('3',"Regular"),
		('4',"Malo"),
		('5',"Muy malo"),
		)
	rendimiento_escolar=models.CharField(choices= rendimiento_escolar_opc,
			default='2',max_length=50)
	asignaturas_actual = models.TextField(blank=False)
	asignatura_preferida = models.CharField(max_length=50)
	asignatura_preferida_porque = models.CharField(max_length=50)
	asignatura_sobresales = models.CharField( max_length=50)
	asignatura_sobresales_porque = models.CharField(max_length=50)
	asignatura_desagrada = models.CharField(max_length=50)
	asignatura_desagrada_porque = models.CharField(max_length=50)
	asignatura_bajopromedio_anterior = models.CharField(max_length=50)
	vienes_tecnologico = models.CharField(max_length=50)
	motiva_venir_tecnologico = models.TextField()

	promedio_anterior = models.FloatField(
		validators = [MinValueValidator(0), MaxValueValidator(100)])


	asignaturas_reprovadas_opc = (
		('si',"Si"),
		('no',"No"),
		)
	asignaturas_reprovadas=models.CharField(choices=asignaturas_reprovadas_opc,
			default='no',max_length=50)	
	asig_reprovadas = models.CharField(max_length=50,blank= True)
	comentarios=JSONField(default={})

class PlanDeVida (UsuarioModelo):
	
	planes_inmediatos = models.TextField(blank= False)
	metas_vida = models.TextField(blank= False)
	#caracteristcaspersonales 
	yo_soy = models.TextField(blank= False)
	mi_caracter = models.TextField(blank= False)
	me_gusta_que = models.TextField(blank= False)
	aspiro_a_que = models.TextField(blank= False)
	miedo_a_que = models.TextField(blank= False)
	podre_lograr_que = models.TextField(blank= False)
	comentarios=JSONField(default={})




