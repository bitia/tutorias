# -*- coding: utf-8 -*-
from django.conf.urls import url,patterns
from .views import DatosPersonalesCreateView

urlpatterns = [
    #   /anexo6/   
    url(r'^nuevo$', DatosPersonalesCreateView.as_view() , name='nuevo'),

]