from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Fortalezas(models.Model):
    nombre = models.CharField(max_length=50)
    usuario = models.ManyToManyField(User)
    def __unicode__(self):
        return "%s "% (self.usuario.username)

class Amenazas(models.Model):
    nombre = models.CharField(max_length=50)
    usuario = models.ManyToManyField(User)
    def __unicode__(self):
        return "%s "% (self.usuario.username)

class Oportunidades(models.Model):
    nombre = models.CharField(max_length=50)
    usuario = models.ManyToManyField(User)
    def __unicode__(self):
        return "%s "% (self.usuario.username)

class Debilidades(models.Model):
    nombre = models.CharField(max_length=50)
    usuario = models.ManyToManyField(User)
    def __unicode__(self):
        return "%s "% (self.usuario.username)


