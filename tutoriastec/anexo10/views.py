from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .forms import fodaForm
import json
from django.http import JsonResponse
from .labels import fort, amenazas, debilidades, oportunidades
from .models import Foda

def ajaxguardar(request):
    if request.method == 'POST':
        if request.is_ajax():

            datos=request.POST.get('foda')
            datos2=request.POST.get('csrfmiddlewaretoken')
            print datos
            print datos2
            #p_fortalezas=datos[0]
            #p_oportunidades=datos[1]
            #p_debilidades=datos[2]
            #p_amenazas=datos[3]
            #print p_fortalezas,p_oportunidades,p_amenazas,p_debilidades

            #fodaUser=Foda(user=request.user,fortaleza=p_fortalezas,oportunidad=p_oportunidades,debilidad=p_debilidades,amenaza=p_amenazas)
            #fodaUser.save()
            #fortalezas=request.POST.get('fortal') 
            #data=request{"email":email , "password" : password}
            #return JsonResponse(data)
            return HttpResponse(
            json.dumps(datos),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def fortalezas_vista(request):
    return render (request,"anexos/anexo10.html",{"fort" : fort,"amen":amenazas,"debi":debilidades,"opor":oportunidades})

##1 recibir los datos y gurdarlos en json en el modelo de fortalezas(mandarle el usuario ...)
##2 formulario de fortalezas , validar los datos, agregar usuario,guardar 
