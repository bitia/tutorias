# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import TestAsertividad
from django import forms
from .labels_verbose import etiqueta

class TestAsertividadForm(ModelForm):

    CHOICES=(
        ('1','Con Frecuencia'),
        ('2','De vez en cuando'),
        ('3','Casi nunca'),
        ('4','Nunca'),
        )
    pregunta1=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect,
        label=etiqueta[0])
    pregunta2=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect,
        label=etiqueta[1])
    pregunta3=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect,
        label=etiqueta[2])
    pregunta4=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect,
        label=etiqueta[3])
    pregunta5=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect,
        label=etiqueta[4])
    pregunta6=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect,
        label=etiqueta[5])
    pregunta7=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect,
        label=etiqueta[6])
    pregunta8=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect,
        label=etiqueta[7])
    pregunta9=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect,
        label=etiqueta[8])
    

    class Meta:
        model = TestAsertividad
        exclude = ["usuario","diagnostico"]