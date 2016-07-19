# -*- coding: utf-8 -*-
from django.conf.urls import url,patterns
from . import views


##anexo12/
urlpatterns = [
    url(r'^parte1$', views.Parte1View.as_view() , name='parte1anexo12'),
    url(r'^gracias$', views.gracias, name='gracias'),
    ]