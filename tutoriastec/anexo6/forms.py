from django import forms
from .models import DatosGenerales, DatosPersonales

class DatosGeneralesForm(forms.ModelForm):
	class Meta:
		model= DatosGenerales
		exclude=["usuario"]

class DatosPersonalesForm(forms.ModelForm):
	class Meta:
		model= DatosPersonales
		exclude=["usuario","fecha"]
