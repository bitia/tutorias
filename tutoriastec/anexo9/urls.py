# -*- coding: utf-8 -*-
from django.conf.urls import url,patterns
from django.views.generic import TemplateView

urlpatterns = [
    #   /anexo9/
    url(r'^linea', TemplateView.as_view(template_name="anexo9/anexo9.html")),
]