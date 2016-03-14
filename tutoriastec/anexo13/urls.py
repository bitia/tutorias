# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    ##  /anexo13/ 
    url(r'hola$', views.hola, name='hola'),
    url(r'gracias$', views.gracias, name='gracias'),
    url(r'diagnostico$', views.diagnostico, name='diagnostico'),
    ]