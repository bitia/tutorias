# -*- coding: utf-8 -*-
from django.conf.urls import url,patterns
from .views import Parte1View, Parte2View

urlpatterns = [
    #   /anexo8/   
    url(r'^parte1$', Parte1View.as_view() , name='anexo8'),
    url(r'^parte2$', Parte2View.as_view() , name='anexo8'),
   # url(r'^parte3$', Parte3View.as_view() , name='anexo8'),
]