"""
tutoriastec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import anexo13
import home
import anexo11
import listaanexos
import anexo6
import anexo8
import anexo12
urlpatterns = [
    url(r'^', include('home.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^anexo13/', include('anexo13.urls')),
    url(r'^anexos/', include('listaanexos.urls')),
    url(r'^anexo11/', include('anexo11.urls')),
    url(r'^anexo6/', include('anexo6.urls')),
    url(r'^anexo10/', include('anexo10.urls')),
    url(r'^anexo8/', include('anexo8.urls')),
    url(r'^anexo9/', include('anexo9.urls')),
    url(r'^anexo12/', include('anexo12.urls')),
]