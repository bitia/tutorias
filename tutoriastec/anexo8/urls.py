# -*- coding: utf-8 -*-
from django.conf.urls import url,patterns
from .views import Parte1View, Parte2View
from django.views.generic import TemplateView

urlpatterns = [
    #   /anexo8/
    url(r'^parte1$', Parte1View.as_view() , name='Parte1View'),
    url(r'^parte2$', Parte2View.as_view() , name='Parte2View'),
    url(r'^partes', TemplateView.as_view(template_name="anexo8/anexo8.html")),
   # url(r'^parte3$', Parte3View.as_view() , name='anexo8'),
]
