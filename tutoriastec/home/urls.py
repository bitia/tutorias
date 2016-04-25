# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    ##  /
    url(r'^$', views.inicio, name='inicio'),
    url(r'^home/$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^anexo6/$', views.registro, name='registro'),
    url(r'^recovery_passwd/$', views.recovery_passwd, name='recovery_passwd'),
    url(r'^log_out/$', views.log_out, name='log_out'),
    url(r'^alumno/perfil$', views.perfil, name='perfil'),
    url(r'^anexos/', TemplateView.as_view(template_name="anexos/anexos.html")),
    url(r'^contacto/', TemplateView.as_view(template_name="contacto.html")),
    ]
