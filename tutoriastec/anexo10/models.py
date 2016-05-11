from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from core.models import UsuarioModelo
class Foda(UsuarioModelo):

    fortalezas = JSONField()
    oportunidades = JSONField()
    debilidades = JSONField()
    amenazas = JSONField()
    comentarios = JSONField()


    def __unicode__(self):
        return "%s "% (self.usuario.username)

