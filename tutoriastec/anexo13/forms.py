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
    pregunta1=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect, 
        label="En una reunión dficil, con con un ambiente tenso,soy capaz de hablar con confianza")
    pregunta2=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect,
        label="Si no estoy segura de una cosa, puedo pedir ayuda facilmente.")
    pregunta3=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect,
        label="Si alguna persona es injusta y agresiva, puedo controlar la situacion con confianza.")
    pregunta4=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect,
        label="si alguna persona se muestra ironica conmigo o con otras, puedo responder sin agresividad")
    pregunta5=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect,
        label="Si creo que se esta abusando de mi, soy capaz de denunciarlo sin alterarme.")
    pregunta6=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect,
        label="Si alguna persona me pide permiso para hacer algo que no me gusta, por ejemplo, fumar, puedo decirle que no sin sentirme culpable")
    pregunta7=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect,
        label="Si alguna persona pide mi opinion sobre alguna cosa me siento bien dandosela, aunque no concuerde con la de los demas")
    pregunta8=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect,
        label="Puedo conectar facil y efectivamente con personas que considero importantes")
    pregunta9=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect,
        label="Cuando encuentro defectos en una tienda o restaurante, soy capaz de exponerlos sin atacar a las otras personas y sin sentirme mal")
    

    class Meta:
        model = TestAsertividad
        exclude = ["usuario","diagnostico"]