#configurando django
=====================

##iniciamos proyecto en django

C:\venv\django1.9.2\Scripts\django-admin.exe  startproject tutoriastec

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
## agregamos carpeta de template
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],


##activar el proyecto
activate.bat

##correrr 
python manage.py runserver 