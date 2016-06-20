from django import forms
from .models import FormatoEntrevista, EstadoPsicofisiologicos, DatosHermanos, AreaIntegracion, CaracteristicasPersonales, AreaPsicopedagogica, PlanDeVida
from django.forms.widgets import NumberInput

class Parte1Form(forms.ModelForm):
    ''' Form FormatoEntrevista'''
    class Meta:
        model= FormatoEntrevista
        exclude=["usuario"]

class Parte2Form(forms.ModelForm):
    ''' EstadoPsicofisiologicos '''
    class Meta:
        model= EstadoPsicofisiologicos
        exclude=["usuario","fecha"]

class Parte3Form(forms.ModelForm):
    ''' DatosHermanos '''
    class Meta:
        model= DatosHermanos
        exclude=["usuario"]

class Parte4Form(forms.ModelForm):
    ''' AreaIntegracion '''
    class Meta:
        model= AreaIntegracion
        exclude=["usuario","fecha"]
        
class Parte5Form(forms.ModelForm):
    ''' CaracteristicasPersonales '''
    class Meta:
        model= CaracteristicasPersonales
        exclude=["usuario","fecha"]

class Parte6Form(forms.ModelForm):
    ''' AreaPsicopedagogica '''
    class Meta:
        model= AreaPsicopedagogica
        exclude=["usuario","fecha"]
        widgets={'promedio_anterior':NumberInput(attrs={"min":'0',"max":'100',"step":'0.5'})}
        
class Parte7Form(forms.ModelForm):
    '''  PlanDeVida '''
    class Meta:
        model= PlanDeVida
        exclude=["usuario","fecha"]