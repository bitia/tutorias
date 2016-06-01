from django.shortcuts import render
from .forms import DatosPersonalesForm
from .models import DatosPersonales, DatosGenerales
from vanilla import ListView, DetailView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

class DatosPersonalesCreateView(CreateView):
    model = DatosPersonales
    form=DatosPersonalesForm

    def get_form(self, data=None, files=None, **kwargs):
        user = self.request.user
        return form(data, files, owner=user, **kwargs)

    def form_valid(self, form):
        send_activation_email(self.request.user)
        account = form.save()
        return HttpResponseRedirect(account.account_activated_url())
"""
class ListDatos(ListView):
    model = DatosPersonales

class CreateDatos(CreateView):
    model = DatosPersonales
    success_url = reverse_lazy('nuevo')

class EditDatos(UpdateView):
    model = DatosPersonales
    success_url = reverse_lazy('modificar')

    DatosPersonalesCreateView(CreateView):
    model=DatosPersonales
    form=DatosPersonalesForm
    fields = ('carrera','numero_control','semestre','fecha')

    def form_valid(self,form):
        self.form=self.form.save()
        self.form.usuario=self.request.user
        self.form.save()
        return super(DatosPersonalesCreateView, self).form_valid(form)


class DatosPersonalesUpDateView(UpdateView):
    model = DatosPersonales
    form=DatosPersonalesForm
    fields = ['usuario','carrera','numero_control','semestre','fecha']
    """
