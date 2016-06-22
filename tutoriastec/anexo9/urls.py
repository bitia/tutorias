# -*- coding: utf-8 -*-
from django.conf.urls import url,patterns
from django.views.generic import TemplateView

urlpatterns = [
    #   /anexo9/
    url(r'^Linea_de_la_vida', TemplateView.as_view(template_name="anexo9/anexo9.html")),
    url(r'^nuevo_suceso', TemplateView.as_view(template_name="anexo9/nuevo_suceso.html")),
    url(r'^grafica', TemplateView.as_view(template_name="anexo9/grafica.html")),
    url(r'^etapas', TemplateView.as_view(template_name="anexo9/etapas.html")),
]
