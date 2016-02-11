from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,"base.html",{"nombre":"bitia"})

def login(request):
	return render(request,"login.html",{"nombre":"bitia"})

def registro(request):
	return render(request,"registro.html",{"nombre":"bitia"})

def recovery_passwd(request):
	return render(request,"recovery_passwd.html",{"nombre":"bitia"})

def perfil(request):
	return render(request,"perfil.html",{"nombre":"bitia"})

