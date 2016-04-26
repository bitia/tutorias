from django.shortcuts import render
from .forms import DatosPersonalesForm
from django.views.generic import CreateView
from .models import DatosPersonales
# Create your views here.

class DatosPersonalesCreateView(CreateView):
    model=DatosPersonales
    form=DatosPersonalesForm
    fields = ('usuario','carrera','numero_control','semestre','fecha')

    def form_valid(self,form):
        self.form=self.form.save()
        self.form.usuario=self.request.user
        self.form.save()
        return super(DatosPersonalesCreateView, self).form_valid(form)