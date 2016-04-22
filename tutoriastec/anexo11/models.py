# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django import forms
from core.models import UsuarioModelo

class OrganizacionEstudio(UsuarioModelo):
    opc_asertividad=(
        ('1','Si'),
        ('0','No'),
        )
    pregunta1=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name="preguntas1")
    pregunta2=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name="preguntas2")
    pregunta3=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name="preguntas3")
    pregunta4=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name="preguntas4") 
    pregunta5=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name="preguntas5")
    pregunta6=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name="preguntas6")
    pregunta7=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name="preguntas7")
    pregunta8=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name="preguntas8") 
    pregunta9=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name="preguntas9")
    pregunta10=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name="preguntas10")
    pregunta11=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name="preguntas11")
    pregunta12=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name="preguntas12")
    pregunta13=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name="preguntas13")
    pregunta14=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name="preguntas14") 
    pregunta15=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name="preguntas15")
    pregunta16=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name="preguntas16")
    pregunta17=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name="preguntas17")
    pregunta18=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name="preguntas18") 
    pregunta19=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name="preguntas19")
    pregunta20=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name="preguntas20")

    DIAGNOSTICO_OPC=(
        ('0','Muy bajo'),
        ('1','bajo'),
        ('2','Por debajo del promedio'),
        ('3','Promedio bajo'),
        ('4','Promedio'),
        ('5','Promedio alto'),
        ('6','Por encima del promedio'),
        ('7','alto'),
        ('8','muy alto'),
        )
    diagnostico=models.CharField(choices=DIAGNOSTICO_OPC,
            blank=True,max_length=2)
    def __unicode__(self):
        return "%s "% (self.usuario.username)
