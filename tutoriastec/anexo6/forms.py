from django import forms
from .models import DatosGenerales, DatosPersonales

class DatosGeneralesForm(forms.ModelForm):
    class Meta:
        model= DatosGenerales
        exclude=["usuario"]
      #  widgets={'numero_hijos':NumberInput(attrs={"min":'0',"max":'10',"step":'1'})}

class DatosPersonalesForm(forms.ModelForm):
    class Meta:
        model= DatosPersonales
        exclude=["usuario","fecha"]
       # widgets={'semestre':NumberInput(attrs={"min":'1',"max":'12',"step":'1'})}