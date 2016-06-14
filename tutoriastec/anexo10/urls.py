# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    ##  /anexo10/ 
    ##  url(r'fortalezas$', views.fortalezas, name='fortalezas'),
    url(r'foda$', views.foda, name='foda'),
    url(r'ajaxguardar$', views.ajaxguardar, name='ajaxguardar'),
    ]