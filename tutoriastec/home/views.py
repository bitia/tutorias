# -*- coding: utf-8 -*-
from django.shortcuts import render
from anexo6.forms import DatosGeneralesForm, DatosPersonalesForm
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as login_auth
from django.http import HttpResponseRedirect as redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
def home(request):
	return render(request,"home/home.html",{})

def inicio(request):
    if request.user.is_authenticated():
        return redirect("/home/")
    return render(request,"base.html",{})

def login(request):
    if request.user.is_authenticated():
        return redirect("/")
    if request.method=='POST':
        usuariof=request.POST['username']
        clavef=request.POST['password']
        print usuariof, clavef
        user=authenticate(username=usuariof,password=clavef)
        if user is not None:
            if user.is_active:
                login_auth(request,user)
                return redirect ("/home/")
            else:
                return render(request,"login.html",{"error":"Lo sentimos al parecer tu cuenta esta Baneada"})
        else:
            return render(request,"login.html",{"error":"Verifica tu usuario o contraseña"})
    else: return render(request,"login.html",{})

@login_required(login_url='/')
def log_out(request):
    logout(request)
    return redirect('/')

def registro(request):
	f_datos_personales= DatosPersonalesForm()
	f_datos_generales=DatosGeneralesForm()
	f_contactos_emergencia=ContactosEmergenciaForm()
	return render(request,"anexos/anexo6.html",{"nombre":"bitia","Form":f_datos_personales,"Form1":f_datos_generales, "Form2": f_contactos_emergencia})

def recovery_passwd(request):
	return render(request,"recovery_passwd.html",{"nombre":"bitia"})

@login_required(login_url='/')
def perfil(request):
	return render(request,"perfil.html",{"nombre":"bitia"})
