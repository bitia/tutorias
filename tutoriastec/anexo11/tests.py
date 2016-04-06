from django.test import TestCase

# Create your tests here.
def nuevos_datos(diccionario):   
    for k,valor in diccionario.items():
        diccionario[k]=random.randint(0,1)
    return diccionario

        org_estudio_data={
        "pregunta1":"1",
        "pregunta2":"1",
        "pregunta3":"1",
        "pregunta4":"1",
        "pregunta5":"1",
        "pregunta6":"1",
        "pregunta7":"1",
        "pregunta8":"1",
        "pregunta9":"1",
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
diagnostico=0

def contar (org_estudio_data):
    for k,valor in org_estudio_data.items():
        if valor==0:
           contador=contador+1
    return contador

def diag_orgestudio(contador):
    if contador ==20:
        msg= "Muy Alto"
        diagnostico="8"
    elif contador >=19 :
        msg="Alto"
        diagnostico="7"
    elif contador >=18 :
        msg="Por encima del promedio"
        diagnostico="6"
    elif contador >=16 :
        msg="Promedio alto"
        diagnostico="5"
    elif contador >=14 :
        msg="Promedio"
        diagnostico="4"
    elif contador >=12 :
        msg="Promedio bajo"
        diagnostico="3"
    elif contador >=11 :
        msg="Por debajo del promedio"
        diagnostico="2"
    elif contador >=10 :
        msg="Bajo"
        diagnostico="1"
    else:
        msg="Muy bajo"
        diagnostico="0"    
    return msg
        