from __future__ import unicode_literals
from django.db import models
from core.models import UsuarioModelo
from django.contrib.postgres.fields import JSONField

class LineadelaVida(UsuarioModelo):
    etapa1 = JSONField(null=True,blank=True,default={})
    etapa2 = JSONField(null=True,blank=True,default={})
    etapa3 = JSONField(null=True,blank=True,default={})
    etapa4 = JSONField(null=True,blank=True,default={})
    comentario = JSONField(null=True,blank=True,default={})

    def __unicode__(self):
        return "%s "% (self.usuario.username)

#periodo:{
#            'sucesos':
#            {
#                'suceso':'aqui el suceso',
#                'animo' :'-2 - +2',  
#                'edad'  :'Y',
#                'orden' :'0-9'
#            }       
#        }
#Y --> rango (inicio del periodo,fin del periodo)
