# -*- coding: utf-8 -*-
from django.conf.urls import url,patterns
from .views import ListDatos, CreateDatos , EditDatos

urlpatterns = [
    #   /anexo6/   
    url(r'^nuevo$', CreateDatos.as_view() , name='nuevo'),
    url(r'^modificar$', EditDatos.as_view() , name='modificar'),

]