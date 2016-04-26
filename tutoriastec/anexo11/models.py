# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django import forms
from core.models import UsuarioModelo
from .labels_verbose import etiquetas1

class OrganizacionEstudio(UsuarioModelo):
    opc_asertividad=(
        ('1','Si'),
        ('0','No'),
        )
    pregunta1=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas1[0])
    pregunta2=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas1[1])
    pregunta3=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas1[2])
    pregunta4=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas1[3]) 
    pregunta5=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas1[4])
    pregunta6=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas1[5])
    pregunta7=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas1[6])
    pregunta8=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas1[7]) 
    pregunta9=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas1[8])
    pregunta10=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas1[9])
    pregunta11=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas1[10])
    pregunta12=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas1[11])
    pregunta13=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas1[12])
    pregunta14=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas1[13]) 
    pregunta15=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas1[14])
    pregunta16=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas1[15])
    pregunta17=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas1[16])
    pregunta18=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas1[17])
    pregunta19=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas1[18])
    pregunta20=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas1[19])

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
