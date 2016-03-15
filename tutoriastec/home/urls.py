# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    ##  /
    url(r'^$', views.inicio, name='inicio'),
    url(r'^home/$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^registro/$', views.registro, name='registro'),
    url(r'^recovery_passwd/$', views.recovery_passwd, name='recovery_passwd'),
    url(r'^log_out/$', views.log_out, name='log_out'),
    url(r'^alumno/perfil$', views.perfil, name='perfil'),
    ]
