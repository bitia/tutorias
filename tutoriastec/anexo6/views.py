from django.shortcuts import render
from .forms import DatosPersonalesForm, DatosGeneralesForm
from .models import DatosPersonales , DatosGenerales
from  django.views.generic  import  View

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
