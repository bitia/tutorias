# -*- coding: utf-8 -*-
from django import forms
from .models import Foda

class fodaForm(forms.ModelForm):
    class Meta:
        model = Foda
        exclude = ["usuario","diagnostico"]