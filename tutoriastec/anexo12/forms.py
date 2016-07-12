# -*- coding: utf-8 -*-
from django import forms
from .models import TestAutoestima
from .labels_verbose import etiquetas1
from .opc_labels import opc_pregunta1

class Parte1Form(forms.ModelForm):
    ''' TestAutoestima '''
    pregunta1 = forms.TypedChoiceField( label=etiquetas1[0],
                     choices=opc_pregunta1, widget=forms.RadioSelect, coerce=int
                )
    class Meta:
        model = TestAutoestima
        exclude = ["usuario","diagnostico"]