# -*- coding: utf-8 -*-
from django.conf.urls import url,patterns
from . import views

urlpatterns = [
    ##  /anexo13/ 
    url(r'hola$', views.ListaOrgEst.as_view(), name='plist'),

    ]