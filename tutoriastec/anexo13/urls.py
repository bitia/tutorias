# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    ##  /anexo13/ 
    url(r'asertividad$', views.asertividadView, name='asertividad'),
    url(r'gracias$', views.gracias, name='gracias'),
    url(r'diagnostico$', views.diagnostico, name='diagnostico'),
    ]