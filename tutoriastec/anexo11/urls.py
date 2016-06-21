# -*- coding: utf-8 -*-
from django.conf.urls import url,patterns
from .views import Parte1View, Parte2View, Parte3View
from django.views.generic import TemplateView

##anexo11/
urlpatterns = [
    url(r'^parte1$', Parte1View.as_view() , name='parte1anexo11'),
    url(r'^parte2$', Parte2View.as_view() , name='parte2anexo11'),
    url(r'^parte3$', Parte3View.as_view() , name='parte3anexo11'),
    url(r'^partes', TemplateView.as_view(template_name="anexo11/anexo11.html")),
]