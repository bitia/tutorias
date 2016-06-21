from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from core.models import UsuarioModelo

class Foda(UsuarioModelo):

    fortaleza = JSONField(null=True,blank=True,default={})
    oportunidad = JSONField(null=True,blank=True,default={})
    debilidad = JSONField(null=True,blank=True,default={})
    amenaza = JSONField(null=True,blank=True,default={})
    comentario = JSONField(null=True,blank=True,default={})
      
    def __unicode__(self):
        return "%s "% (self.usuario.username)

