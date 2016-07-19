from __future__ import unicode_literals
from django.db import models
from django.contrib.postgres.fields import JSONField
from core.models import UsuarioModelo
from .labels_verbose import etiquetas1
from .opc_labels import opc_pregunta1,opc_pregunta2,opc_pregunta3,opc_pregunta4,opc_pregunta5,opc_pregunta6,opc_pregunta7,opc_pregunta8,opc_pregunta9,opc_pregunta10
# Create your models here.
class TestAutoestima(UsuarioModelo):

    pregunta1=models.CharField(choices=opc_pregunta1,
            blank=False,max_length=2,verbose_name=etiquetas1[0])
    pregunta2=models.CharField(choices=opc_pregunta2,
            blank=False,max_length=2,verbose_name=etiquetas1[1])
    pregunta3=models.CharField(choices=opc_pregunta3,
            blank=False,max_length=2,verbose_name=etiquetas1[2])
    pregunta4=models.CharField(choices=opc_pregunta4,
            blank=False,max_length=2,verbose_name=etiquetas1[3]) 
    pregunta5=models.CharField(choices=opc_pregunta5,
            blank=False,max_length=2,verbose_name=etiquetas1[4])
    pregunta6=models.CharField(choices=opc_pregunta6,
            blank=False,max_length=2,verbose_name=etiquetas1[5])
    pregunta7=models.CharField(choices=opc_pregunta7,
            blank=False,max_length=2,verbose_name=etiquetas1[6])
    pregunta8=models.CharField(choices=opc_pregunta8,
            blank=False,max_length=2,verbose_name=etiquetas1[7]) 
    pregunta9=models.CharField(choices=opc_pregunta9,
            blank=False,max_length=2,verbose_name=etiquetas1[8])
    pregunta10=models.CharField(choices=opc_pregunta10,
            blank=False,max_length=2,verbose_name=etiquetas1[9])

    DIAGNOSTICO_OPC=(
        ('1','Tienes un nivel algo bajo de autoestima.'),
        ('2','Tu nivel de autoestima es suficiente.'),
        ('3','Tu nivel de autoestima es muy bueno.'),
        ('4','Tienes un alto nivel de autoestima y mucha confianza y seguridad en ti mismo.'),
        )
    diagnostico=models.CharField(choices=DIAGNOSTICO_OPC,
            blank=True,max_length=2)
    comentarios = JSONField(default={},blank=True)
    
    #def __unicode__(self):
        #return "%s "% (self.usuario.username)