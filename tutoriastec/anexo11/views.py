from django.shortcuts import render
from  django.http  import  HttpResponseRedirect
from  django.views.generic  import  View
from .forms import OrgEstudioForm, TecEstudioForm, MotEstudioForm
# Create your views here.
class OrgStudioView(View):
    form_class= OrgEstudioForm
    initial=''
    errores=[]
<<<<<<< HEAD
    template_name = 'anexos/anexo11.html'
=======
    template_name = 'anexo11/Parte1.html'
>>>>>>> b9682feb5189956e3ff1359bf01aefe9745b7adb
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
