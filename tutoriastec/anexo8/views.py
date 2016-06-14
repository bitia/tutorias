from django.shortcuts import render
from .forms import Parte1Form, Parte2Form, Parte3Form, Parte4Form, Parte5Form, Parte6Form, Parte7Form
from  django.views.generic  import  View

class Parte1View(View):
    form_class=Parte1Form
    initial=''
    errores=[]
    template_name = 'anexo8/parte1.html'
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

class Parte2View(View):
    form_class=Parte2Form
    initial=''
    errores=[]
    template_name = 'anexo8/parte2.html'
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
