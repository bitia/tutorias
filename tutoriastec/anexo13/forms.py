from django.forms import ModelForm
from .models import TestAsertividad
from django import forms

class TestAsertividadForm(ModelForm):
    class Meta:
        model = TestAsertividad
        exclude = ["usuario","diagnostico"]