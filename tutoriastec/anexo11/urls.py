# -*- coding: utf-8 -*-
from django.conf.urls import url,patterns
from .views import OrgStudioView

##anexo11/
urlpatterns = [
    url(r'^parte1$', OrgStudioView.as_view() , name='anexo11'),

]