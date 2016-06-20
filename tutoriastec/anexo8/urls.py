# -*- coding: utf-8 -*-
from django.conf.urls import url,patterns
from .views import Parte1View, Parte2View,Parte3View,Parte3View, Parte4View, Parte5View, Parte6View, Parte7View
from django.views.generic import TemplateView

urlpatterns = [
    #   /anexo8/
    url(r'^parte1$', Parte1View.as_view() , name='Parte1View'),
    url(r'^parte2$', Parte2View.as_view() , name='Parte2View'),
    url(r'^parte3$', Parte3View.as_view() , name='Parte3View'),
    url(r'^parte4$', Parte4View.as_view() , name='Parte4View'),
    url(r'^parte5$', Parte5View.as_view() , name='Parte5View'),
    url(r'^parte6$', Parte6View.as_view() , name='Parte6View'),
    url(r'^parte7$', Parte7View.as_view() , name='Parte7View'),
    url(r'^partes', TemplateView.as_view(template_name="anexo8/anexo8.html")),
]
