# -*- coding: utf-8 -*-
from django.conf.urls import url,patterns
from .views import Anexo6View

urlpatterns = [
    #   /anexo6/   
    url(r'^nuevo$', Anexo6View.as_view() , name='anexo6'),


]