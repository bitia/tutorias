# -*- coding: utf-8 -*-
from django.conf.urls import url,patterns
from .views import OrgStudioView


urlpatterns = [
    url(r'^$', OrgStudioView.as_view() , name='anexo11'),

]