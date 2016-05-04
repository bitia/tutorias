# -*- coding: utf-8 -*-
from django import forms
from .models import OrganizacionEstudio, TecnicasEstudio, MotivacionEstudio

class OrgEstudioForm(forms.ModelForm):
    class Meta:
        model = OrganizacionEstudio
        exclude = ["usuario","diagnostico"]

class TecEstudioForm(forms.ModelForm):
    class Meta:
        model = TecnicasEstudio
        exclude = ["usuario","diagnostico"]

class MotEstudioForm(forms.ModelForm):
    class Meta:
        model = MotivacionEstudio
        exclude = ["usuario","diagnostico"]