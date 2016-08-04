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

#    tabla=["I","II","III","IV","V"]

def valores(tipo,contador):
    calificacion=""
    lis2=[]
    datos=[[20,20,20,[57,60],"Muy alto"],
    [19,[18,19],19,[52,56],"Alto"],
    [18,17,18,[50,51],"Por encima del promedio"],
    [[16,17],16,17,[48,49],"promedio alto"],
    [[14,15],[14,15],16,[43,47],"Promedio"],
    [[12,13],13,15,[39,42],"Promedio bajo"],
    [11,12,[13,14],[37,38],"Por debajo del promedio"],
    [10,11,12,[34,36],"Bajo"],
    [[0,9],[0,10],[0,11],[0,33],"Muy alto"]]

    for i in range(0,8):
        if type(datos[i][tipo]) is int:
            if contador==datos[i][tipo]:
                calificacion=datos[i][4]
        else:
            lis2=datos[i][tipo]
            if contador>=lis2[0] and contador<=lis2[1]:
                calificacion=datos[i][4]
    return calificacion
    


    def removercampos(anexo ,*args):
        for c, campo in enumerate(args):
        anexo.pop(campo)
    return anexo


