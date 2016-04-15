# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    ##  /anexos/ 
    ##url(r'^$', views.listaanexos, name='listaanexos'),
    url(r'lista$', views.listaanexos, name='listaanexos'),
    ]