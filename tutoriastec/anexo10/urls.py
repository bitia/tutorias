# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    ##  /anexo10/ 
    ##  url(r'fortalezas$', views.fortalezas, name='fortalezas'),
    url(r'fortalezas_vista$', views.fortalezas_vista, name='fortalezas_vista'),
    url(r'ajaxguardar$', views.ajaxguardar, name='ajaxguardar'),
    ]