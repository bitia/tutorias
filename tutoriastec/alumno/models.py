from __future__ import unicode_literals
from django.contrib.auth.models import User, UserManager
from django.db import models


class AlumnoUser(User):
    """User with app settings."""
    # firstname nombre = models.CharField(max_length=50)
    # username num_control = models.CharField(max_length=10)
    #lastname = models.CharField(max_length=10)
    #email
    carrera = models.CharField(max_length=50)
    semestre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=2)
    #password
    telefono = models.CharField(max_length=10)

    # Use UserManager to get the create_user method, etc.
    objects = UserManager()
    