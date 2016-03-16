# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import TestAsertividad
from django import forms

class TestAsertividadForm(ModelForm):
    CHOICES=(
        ('1','Con Frecuencia'),
        ('2','De vez en cuando'),
        ('3','Casi nunca'),
        ('4','Nunca'),
        )
    pregunta1 = forms.ChoiceField(widget=forms.RadioSelect, 
        choices=CHOICES,
        label="En una reunión dficil, con con un ambiente tenso,soy capaz de hablar con confianza")
    
    class Meta:
        model = TestAsertividad
        exclude = ["usuario","diagnostico"]