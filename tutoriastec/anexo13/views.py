from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TestAsertividadForm
from .models import TestAsertividad


# Create your views here.
@login_required(login_url='/')
def hola(request):
    usuario=request.user
    errores=[]
    if request.method=='POST':
        print ( "entre al post")
        try :
            userTest= TestAsertividad.objects.get(usuario = usuario)
            f_asertividad=TestAsertividadForm(request.POST,instance =userTest)
        except:
            f_asertividad = TestAsertividadForm(request.POST)
        
        if f_asertividad.is_valid():
            print ("es valido el formulario")
            form=f_asertividad.save()
            form.usuario=usuario
            form.save()

            return redirect("/anexo13/gracias")

        else:

            errores.append(f_asertividad.errors)
            print ("No es valido el formulario")
            print(errores)
            return render(request,"anexos/asertividad.html", {"form":f_asertividad})
    else:
        try:
            userTest= TestAsertividad.objects.get(usuario = usuario)
            f_asertividad=TestAsertividadForm(instance =userTest)
            print("usuario si tiene test ")
            return render(request,"anexos/asertividad.html", {"form":f_asertividad})
        except:
            print("usuario no tiene test ")
            f_asertividad=TestAsertividadForm()
            return render(request,"anexos/asertividad.html", {"form":f_asertividad})

def gracias(request):
    return render(request,"anexos/gracias.html", {"mensaje":"gracias por llenar el test de asertividad"})

def diagnostico(request):
    usuario=request.user

    return render(request,"anexos/diagnostico.html")