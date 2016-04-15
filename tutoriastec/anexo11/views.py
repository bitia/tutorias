from django.shortcuts import render
from  django.http  import  HttpResponseRedirect 
from  django.views.generic  import  View
from models import OrganizacionEstudio
from .forms import OrgEstudioForm
# Create your views here.

class OrgStudioView(View):
    Form= OrgEstudioForm
    initial=''


    def diagnostico(request):
        org_estudio_data={
        "pregunta1":"0",
        "pregunta2":"0",
        "pregunta3":"0",
        "pregunta4":"0",
        "pregunta5":"0",
        "pregunta6":"0",
        "pregunta7":"0",
        "pregunta8":"0",
        "pregunta9":"0",
        "pregunta10":"0",
        "pregunta11":"0",
        "pregunta12":"0",
        "pregunta13":"0",
        "pregunta14":"0",
        "pregunta15":"0",
        "pregunta16":"0",
        "pregunta17":"0",
        "pregunta18":"0",
        "pregunta19":"0",
        "pregunta20":"0",
        }
        contador=0
        for k,valor in org_estudio_data.items():
            if valor=="0":
                contador=contador+1

        if contador == 20:
            msg= "Muy Alto"
            encuesta.diagnostico="8"
        elif contador >=19 :
            msg="Alto"
            encuesta.diagnostico="7"
        elif contador >=18 :
            msg="Por encima del promedio"
            encuesta.diagnostico="6"
        elif contador >=16 :
            msg="Promedio alto"
            encuesta.diagnostico="5"
        elif contador >=14 :
            msg="Promedio"
            encuesta.diagnostico="4"
        elif contador >=12 :
            msg="Promedio bajo"
            encuesta.diagnostico="3"
        elif contador >=11 :
            msg="Por debajo del promedio"
            encuesta.diagnostico="2"
        elif contador >=10 :
            msg="Bajo"
            encuesta.diagnostico="1"
        else:
            msg="Muy bajo"
            encuesta.diagnostico="0"
        
        print ( msg, contador)
        
        return render(request,"anexos/diagnostico.html",{"mensaje":msg})

    def removercampos(anexo ,*args):
            for c, campo in enumerate(args):
            anexo.pop(campo)
        return anexo

        
        pass