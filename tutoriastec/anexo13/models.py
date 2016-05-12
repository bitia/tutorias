# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django import forms
from .labels_verbose import etiqueta
from django.contrib.postgres.fields import JSONField
from core.models import UsuarioModelo

class TestAsertividad (UsuarioModelo):
	opc_asertividad=(
		('1','Con Frecuencia'),
		('2','De vez en cuando'),
		('3','Casi nunca'),
		('4','Nunca'),
		)
	pregunta1=models.CharField(choices=opc_asertividad,default ='4',
			blank=False,max_length=2,verbose_name=etiqueta[0])
	pregunta2=models.CharField(choices=opc_asertividad,default ='4',
			blank=False,max_length=2,verbose_name=etiqueta[1])
	pregunta3=models.CharField(choices=opc_asertividad,default ='4',
			blank=False,max_length=2,verbose_name=etiqueta[2])
	pregunta4=models.CharField(choices=opc_asertividad,default ='4',
			blank=False,max_length=2,verbose_name=etiqueta[3])
	pregunta5=models.CharField(choices=opc_asertividad,default ='4',
			blank=False,max_length=2,verbose_name=etiqueta[4])
	pregunta6=models.CharField(choices=opc_asertividad,default ='4',
			blank=False,max_length=2,verbose_name=etiqueta[5])
	pregunta7=models.CharField(choices=opc_asertividad,default ='4',
			blank=False,max_length=2,verbose_name=etiqueta[6])
	pregunta8=models.CharField(choices=opc_asertividad,default ='4',
			blank=False,max_length=2,verbose_name=etiqueta[7])
	pregunta9=models.CharField(choices=opc_asertividad,default ='4',
			blank=False,max_length=2,verbose_name=etiqueta[8])
	
	DIAGNOSTICO_OPC=(
		('1','Paso el Test de asertividad'),
		('0','No paso el Test de asertividad'),
		)
	
	diagnostico=models.CharField(choices=DIAGNOSTICO_OPC,
			blank=True,max_length=2)
	comentarios = JSONField(null=True,blank=True,default={})

	def __unicode__(self):
		return "%s "% (self.usuario.username)

