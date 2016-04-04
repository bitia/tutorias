# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.
class TestAsertividad (models.Model):
	usuario = models.OneToOneField(User,blank=True, null= True, on_delete=models.CASCADE)

	opc_asertividad=(
		('1','Con Frecuencia'),
		('2','De vez en cuando'),
		('3','Casi nunca'),
		('4','Nunca'),
		)
	pregunta1=models.CharField(choices=opc_asertividad,default ='4',
			blank=False,max_length=2,verbose_name="En una reunión dficil, con con un ambiente tenso,soy capaz de hablar con confianza")
	pregunta2=models.CharField(choices=opc_asertividad,default ='4',
			blank=False,max_length=2,verbose_name="Si no estoy segura de una cosa, puedo pedir ayuda facilmente.")
	pregunta3=models.CharField(choices=opc_asertividad,default ='4',
			blank=False,max_length=2,verbose_name="Si alguna persona es injusta y agresiva, puedo controlar la situacion con confianza.")
	pregunta4=models.CharField(choices=opc_asertividad,default ='4',
			blank=False,max_length=2,verbose_name="si alguna persona se muestra ironica conmigo o con otras, puedo responder sin agresividad")
	pregunta5=models.CharField(choices=opc_asertividad,default ='4',
			blank=False,max_length=2,verbose_name="Si creo que se esta abusando de mi, soy capaz de denunciarlo sin alterarme.")
	pregunta6=models.CharField(choices=opc_asertividad,default ='4',
			blank=False,max_length=2,verbose_name="Si alguna persona me pide permiso para hacer algo que no me gusta, por ejemplo, fumar, puedo decirle que no sin sentirme culpable")
	pregunta7=models.CharField(choices=opc_asertividad,default ='4',
			blank=False,max_length=2,verbose_name="Si alguna persona pide mi opinion sobre alguna cosa me siento bien dandosela, aunque no concuerde con la de los demas")
	pregunta8=models.CharField(choices=opc_asertividad,default ='4',
			blank=False,max_length=2,verbose_name="Puedo conectar facil y efectivamente con personas que considero importantes")
	pregunta9=models.CharField(choices=opc_asertividad,default ='4',
			blank=False,max_length=2,verbose_name="Cuando encuentro defectos en una tienda o restaurante, soy capaz de exponerlos sin atacar a las otras personas y sin sentirme mal")
	
	DIAGNOSTICO_OPC=(
		('1','Paso el Test de asertividad'),
		('0','No paso el Test de asertividad'),
		)
	diagnostico=models.CharField(choices=DIAGNOSTICO_OPC,
			blank=True,max_length=2)


	def __unicode__(self):
		return "%s "% (self.usuario.username)

class Comentarios(models.Model):
	tutorado = models.ForeignKey(User,related_name='+',blank=True)
	tutor= models.ForeignKey(User,related_name='+',blank=True)
	comentario = models.TextField()
