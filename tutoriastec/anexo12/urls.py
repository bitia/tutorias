# -*- coding: utf-8 -*-
from django.conf.urls import url,patterns
from .views import Parte1View

##anexo12/
urlpatterns = [
    url(r'^parte1$', Parte1View.as_view() , name='parte1anexo12'),
    ]