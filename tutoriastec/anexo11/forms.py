# -*- coding: utf-8 -*-
from django import forms
from .models import OrganizacionEstudio, TecnicasEstudio, MotivacionEstudio, InventarioEstudio

class Parte1Form(forms.ModelForm):
    ''' OrganizacionEstudio '''
    class Meta:
        model = OrganizacionEstudio
        exclude = ["usuario","diagnostico"]

class Parte2Form(forms.ModelForm):
    ''' TecnicasEstudio '''
    class Meta:
        model = TecnicasEstudio
        exclude = ["usuario","diagnostico"]

class Parte3Form(forms.ModelForm):
    ''' MotivacionEstudio '''
    class Meta:
        model = MotivacionEstudio
        exclude = ["usuario","diagnostico"]

class Parte4Form(forms.ModelForm):
    ''' InventarioEstudio '''
    class Meta:
        model = InventarioEstudio
        exclude = ["usuario","diagnostico"]