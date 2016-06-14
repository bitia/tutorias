from django.db import models
from django.contrib.auth.models import User


class UsuarioModelo(models.Model):

    usuario=models.OneToOneField(User,blank=True, null= True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class TiempoModelo(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True