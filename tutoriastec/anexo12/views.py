from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from  django.http  import  HttpResponseRedirect
from  django.views.generic  import  View
from .forms import Parte1Form
from .models import TestAutoestima

#@login_required(login_url='/')
class Parte1View(View):
    ''' TestAutoestima '''
    form_class= Parte1Form
    initial=''
    errores=[]
    template_name = 'anexo12/parte1.html'
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = self.form_class(request.POST)
        usuario=request.user
        if form.is_valid():
            form=form.save()
            form.usuario=usuario
            form.save()
            
            resultado= diagnostico(form)
            form.diagnostico=str(resultado)
            form.save(update_fields=["diagnostico"])
            print(resultado)
            return HttpResponseRedirect("/anexos/gracias/")
        else:
            self.errores.append(form.errors)
            print ("No es valido el formulario")
            print(self.errores)
            return render(request, self.template_name, {'form': form})

def diagnostico(formulario):
    resultado=0
    cont1=0
    cont2=0
    cont3=0
    cont4=0 

    form=formulario.__dict__
    for p,v in form.items():
        if (p=="_usuario_cache" or p=="comentarios" or p=="diagnostico" or p=="created" or p=="usuario_id" or p=="id" or p=="modified"):
            pass
        if v=='1' :
            cont1=cont1 + 1
        elif v=='2' :
            cont2=cont2 + 1
        elif v=='3' :
            cont3=cont3 + 1
        elif v=='4' :
            cont4=cont4 + 1

    tupla=(cont1,cont2,cont3,cont4)
    resultado=max(tupla)
    return resultado
    
def gracias(request):
    return render(request,"anexos/gracias.html", {"mensaje":"gracias por llenar el test de asertividad"})
