# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django import forms
from core.models import UsuarioModelo
from .labels_verbose import etiquetas1,etiquetas2,etiquetas3,etiquetas4
from django.contrib.postgres.fields import JSONField

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
    
    comentarios = JSONField(default={})
    def __unicode__(self):
        return "%s "% (self.usuario.username)

class TecnicasEstudio(UsuarioModelo):
    opc_asertividad=(
        ('1','Si'),
        ('0','No'),
        )
    pregunta1=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas2[0])
    pregunta2=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas2[1])
    pregunta3=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas2[2])
    pregunta4=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas2[3]) 
    pregunta5=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas2[4])
    pregunta6=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas2[5])
    pregunta7=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas2[6])
    pregunta8=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas2[7]) 
    pregunta9=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas2[8])
    pregunta10=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas2[9])
    pregunta11=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas2[10])
    pregunta12=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas2[11])
    pregunta13=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas2[12])
    pregunta14=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas2[13]) 
    pregunta15=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas2[14])
    pregunta16=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas2[15])
    pregunta17=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas2[16])
    pregunta18=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas2[17])
    pregunta19=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas2[18])
    pregunta20=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas2[19])
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
    comentarios = JSONField(default={})
    def __unicode__(self):
        return "%s "% (self.usuario.username)

class MotivacionEstudio(UsuarioModelo):
    opc_asertividad=(
        ('1','Si'),
        ('0','No'),
        )

    pregunta1=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas3[0])
    pregunta2=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas3[1])
    pregunta3=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas3[2])
    pregunta4=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas3[3]) 
    pregunta5=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas3[4])
    pregunta6=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas3[5])
    pregunta7=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas3[6])
    pregunta8=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas3[7]) 
    pregunta9=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas3[8])
    pregunta10=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas3[9])
    pregunta11=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas3[10])
    pregunta12=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas3[11])
    pregunta13=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas3[12])
    pregunta14=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas3[13]) 
    pregunta15=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas3[14])
    pregunta16=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas3[15])
    pregunta17=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas3[16])
    pregunta18=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas3[17])
    pregunta19=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas3[18])
    pregunta20=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas3[19])

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

    comentarios = JSONField(default={})
    def __unicode__(self):
        return "%s "% (self.usuario.username)

class InventarioEstudio(UsuarioModelo):

    opc_inv=(
        ('1','Nunca'),
        ('2','Raramente'),
        ('3','Ocacionalmente'),
        ('4','Usualmente'),
        ('5','Siempre'),
        )
    pregunta1=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[0])
    pregunta2=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[1])
    pregunta3=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[2])
    pregunta4=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[3])
    pregunta5=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[4])
    pregunta6=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[5])
    pregunta7=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[6])
    pregunta8=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[7])
    pregunta9=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[8])
    pregunta10=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[9])
    pregunta11=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[10])
    pregunta12=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[11])
    pregunta13=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[12])
    pregunta14=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[13])
    pregunta15=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[14])
    pregunta16=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[15])
    pregunta17=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[16])
    pregunta18=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[17])
    pregunta19=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[18])
    pregunta20=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[19])
    pregunta21=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[20])
    pregunta22=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[21])
    pregunta23=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[22])
    pregunta24=models.CharField(choices=opc_inv,
            blank=False,max_length=2,verbose_name=etiquetas4[23]) 


    DIAGNOSTICO_OPC=(
        ('0','Visual'),
        ('1','Auditivo'),
        ('2','Kinestesico'),
        )
    diagnostico=models.CharField(choices=DIAGNOSTICO_OPC,
            blank=True,max_length=2)

    comentarios = JSONField(default={})
    def __unicode__(self):
        return "%s "% (self.usuario.username)