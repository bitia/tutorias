from __future__ import unicode_literals
from core.models import UsuarioModelo
from django.db import models
from django.contrib.postgres.fields import ArrayField

class  DesempenioAcademico(UsuarioModelo):

    ''' Anexo 15 '''
    materia1 = ArrayField(ArrayField(models.IntegerField()))
    materia2 = ArrayField(ArrayField(models.IntegerField()))
    materia3 = ArrayField(ArrayField(models.IntegerField()))
    materia4 = ArrayField(ArrayField(models.IntegerField()))
    materia5 = ArrayField(ArrayField(models.IntegerField()))
    materia6 = ArrayField(ArrayField(models.IntegerField()))
    materia7 = ArrayField(ArrayField(models.IntegerField()))
    
    comentarios = JSONField(null=True,blank=True,default={})

    def __unicode__(self):
        return "%s "% (self.usuario.username)

