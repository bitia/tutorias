from django import forms
from .models import ContactosEmergencia, DatosGenerales, DatosPersonales

class ContactosEmergenciaForm(forms.ModelForm):
	class Meta:
		model= ContactosEmergencia
		exclude=["usuario"]

class DatosGeneralesForm(forms.ModelForm):
	class Meta:
		model= DatosGenerales
		exclude=["usuario"]

class DatosPersonalesForm(forms.ModelForm):
	class Meta:
		model= DatosPersonales
		exclude=["usuario","fecha"]
