# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import OrganizacionEstudio
from django import forms

class OrgEstudioForm(ModelForm):
    
    class Meta:
        model = OrganizacionEstudio
        exclude = ["usuario","diagnostico"]