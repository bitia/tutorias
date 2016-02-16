from django import forms 
from .models import ContactosEmergencia, DatosGenerales, DatosPersonales

class ContactosEmergenciaForm(forms.ModelForm):
	class Meta:
		model= ContactosEmergencia
		exclude=["telefono"]

class DatosGeneralesForm(forms.ModelForm):
	class Meta:
		model= DatosGenerales
		exclude=["telefono"]

class DatosPersonalesForm(forms.ModelForm):
	class Meta:
		model= DatosPersonales
		exclude=["fecha"]
