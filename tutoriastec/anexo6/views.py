from django.shortcuts import render
from .forms import DatosPersonalesForm, DatosGeneralesForm
from .models import DatosPersonales , DatosGenerales
from  django.views.generic  import  View
from  django.http  import  HttpResponseRedirect
from django.utils import timezone

class Anexo6View(View):
    form_class=DatosPersonalesForm
    form_class2=DatosGeneralesForm
    initial=''
    errores=[]
    template_name = 'anexo6/Parte1.html'
    def get(self, request):
        form = self.form_class(initial=self.initial)
        form2= self.form_class2(initial=self.initial)
        return render(request, self.template_name, {'form': form,'form2': form2})
    def post(self, request):
        form = self.form_class(request.POST)
        form2 = self.form_class2(request.POST)
        usuario=request.user
        #print form2.trabajas_horario_inicio
        #print form2.trabajas_horario_salida
        #print form2.fecha_nacimiento
        if form.is_valid() and form2.is_valid():
            form=form.save()
            form2=form2.save()
            form.usuario=usuario
            form.save()
            form2.usuario=usuario
            form2.save()
            return HttpResponseRedirect("/anexo13/gracias/")
        else:
            self.errores.append(form.errors)
            self.errores.append(form2.errors)
            print ("No es valido el formulario")
            print(self.errores)
            return render(request, self.template_name, {'form': form})