#configurando django
=====================
##agregando una app

(django1.9.2) C:\proyectos\tutorias\tutoriastec>python manage.py startapp home


##agregar una app al archivo setings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
]
