from django.forms import ModelForm
from .models import TestAsertividad

class TestAsertividadForm(ModelForm):
    class Meta:
        model = TestAsertividad
        exclude = ["usuario","diagnostico"]
