"""tutoriastec URL Configuration

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
from home import views
import anexo13

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.inicio, name='inicio'),
    url(r'^login/$', views.login, name='login'),
    url(r'^registro/$', views.registro, name='registro'),
    url(r'^recovery_passwd/$', views.recovery_passwd, name='recovery_passwd'),
    url(r'^alumno/perfil$', views.perfil, name='perfil'),
    url(r'^anexo13/', include('anexo13.urls')),
    url(r'^log_out/$', views.log_out, name='log_out'),
    url(r'^home/$', views.home, name='home'),




    
]
