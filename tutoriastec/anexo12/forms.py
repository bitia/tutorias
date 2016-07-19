# -*- coding: utf-8 -*-
from django import forms
from .models import TestAutoestima
from .labels_verbose import etiquetas1
from .opc_labels import opc_pregunta1,opc_pregunta2,opc_pregunta3,opc_pregunta4,opc_pregunta5,opc_pregunta6,opc_pregunta7,opc_pregunta8,opc_pregunta9,opc_pregunta10

class Parte1Form(forms.ModelForm):
    ''' TestAutoestima '''
    pregunta1 = forms.TypedChoiceField( label=etiquetas1[0],
                     choices=opc_pregunta1, widget=forms.RadioSelect, coerce=int
                )
    pregunta2 = forms.TypedChoiceField( label=etiquetas1[1],
        choices=opc_pregunta2, widget=forms.RadioSelect, coerce=int)
    pregunta3 = forms.TypedChoiceField( label=etiquetas1[2],
        choices=opc_pregunta3, widget=forms.RadioSelect, coerce=int)
    pregunta4 = forms.TypedChoiceField( label=etiquetas1[3],
        choices=opc_pregunta4, widget=forms.RadioSelect, coerce=int)
    pregunta5 = forms.TypedChoiceField( label=etiquetas1[4],
        choices=opc_pregunta5, widget=forms.RadioSelect, coerce=int)
    pregunta6 = forms.TypedChoiceField( label=etiquetas1[5],
        choices=opc_pregunta6, widget=forms.RadioSelect, coerce=int)
    pregunta7 = forms.TypedChoiceField( label=etiquetas1[6],
        choices=opc_pregunta7, widget=forms.RadioSelect, coerce=int)
    pregunta8 = forms.TypedChoiceField( label=etiquetas1[7],
        choices=opc_pregunta8, widget=forms.RadioSelect, coerce=int)
    pregunta9 = forms.TypedChoiceField( label=etiquetas1[8],
        choices=opc_pregunta9, widget=forms.RadioSelect, coerce=int)
    pregunta10 = forms.TypedChoiceField( label=etiquetas1[9],
        choices=opc_pregunta10, widget=forms.RadioSelect, coerce=int)
    class Meta:
        model = TestAutoestima
        exclude = ["usuario","diagnostico"]