from django.contrib import admin
from .models import DatosPersonales,DatosGenerales
# Register your models here.
admin.site.register(DatosPersonales)
admin.site.register(DatosGenerales)