from django.shortcuts import render
from anexo6.forms import ContactosEmergenciaForm, DatosGeneralesForm, DatosPersonalesForm

# Create your views here.
def home(request):
	return render(request,"base.html",{"nombre":"bitia"})

def login(request):
	return render(request,"login.html",{"nombre":"bitia"})

def registro(request):
	f_datos_personales= DatosPersonalesForm()
	return render(request,"registro.html",{"nombre":"bitia","Form":f_datos_personales})

def recovery_passwd(request):
	return render(request,"recovery_passwd.html",{"nombre":"bitia"})

def perfil(request):
	return render(request,"perfil.html",{"nombre":"bitia"})

