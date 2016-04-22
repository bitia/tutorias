from django.contrib import admin
from .models import Amenazas, Debilidades, Fortalezas, Oportunidades
# Register your models here.
admin.site.register(Amenazas)
admin.site.register(Debilidades)
admin.site.register(Fortalezas)
admin.site.register(Oportunidades)