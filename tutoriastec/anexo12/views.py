from django.shortcuts import render
from  django.http  import  HttpResponseRedirect
from  django.views.generic  import  View
from .forms import Parte1Form

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
            return HttpResponseRedirect("/anexo13/gracias/")
        else:
            self.errores.append(form.errors)
            print ("No es valido el formulario")
            print(self.errores)
            return render(request, self.template_name, {'form': form})