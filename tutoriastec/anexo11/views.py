from django.shortcuts import render
from  django.http  import  HttpResponseRedirect
from  django.views.generic  import  View
from .forms import Parte1Form, Parte2Form, Parte3Form, Parte4Form

class Parte1View(View):
    ''' OrganizacionEstudio '''
    form_class= Parte1Form
    initial=''
    errores=[]
    template_name = 'anexo11/parte1.html'
    cont=0
    respuesta=0

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = self.form_class(request.POST)
        usuario=request.user
        if form.is_valid():
            form=form.save()
            form.usuario=usuario
            form.save()

            cont=Contador(form)
            respuesta=valores(0,cont)
            print("contando los no    ",cont, "Respuesta      ",respuesta)
            form.diagnostico=respuesta
            form.save(update_fields=["diagnostico"])
            print("guardado")

            return HttpResponseRedirect("/anexo13/gracias/")
        else:
            self.errores.append(form.errors)
            print ("No es valido el formulario")
            print(self.errores)
            return render(request, self.template_name, {'form': form})

class Parte2View(View):
    ''' TecnicasEstudio '''
    form_class=Parte2Form
    initial=''
    errores=[]
    template_name = 'anexo11/parte2.html'
    cont=0
    respuesta=0

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = self.form_class(request.POST)
        usuario=request.user
        if form.is_valid():
            form=form.save()
            form.usuario=usuario
            form.save()

            cont=Contador(form)
            respuesta=valores(1,cont)
            print("contando los no    ",cont, "Respuesta      ",respuesta)
            form.diagnostico=respuesta
            form.save(update_fields=["diagnostico"])
            print("guardado")

            return HttpResponseRedirect("/anexo13/gracias/")
        else:
            self.errores.append(form.errors)
            print ("No es valido el formulario")
            print(self.errores)
            return render(request, self.template_name, {'form': form})

class Parte3View(View):
    ''' MotivacionEstudio '''
    form_class=Parte3Form
    initial=''
    errores=[]
    template_name = 'anexo11/parte3.html'
    cont=0
    respuesta=0

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = self.form_class(request.POST)
        usuario=request.user
        if form.is_valid():
            form=form.save()
            form.usuario=usuario
            form.save()

            cont=Contador(form)
            respuesta=valores(2,cont)
            print("contando los no    ",cont, "Respuesta      ",respuesta)
            form.diagnostico=respuesta
            form.save(update_fields=["diagnostico"])
            print("guardado")
            return HttpResponseRedirect("/anexo13/gracias/")
        else:
            self.errores.append(form.errors)
            print ("No es valido el formulario")
            print(self.errores)
            return render(request, self.template_name, {'form': form})

class Parte4View(View):
    ''' InventarioEstudio '''
    form_class=Parte4Form
    initial=''
    errores=[]
    template_name = 'anexo11/parte4.html'
    resultados=[0,0,0]

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = self.form_class(request.POST)
        usuario=request.user
        if form.is_valid() : 
            form=form.save()
            form.usuario=usuario
            form.save()
            resultados=diagnosticoInventerioE(form)
            print ("resultados :   ",resultados)

            form.diagnostico_Visual=resultados[0]
            form.diagnostico_Auditivo=resultados[1]
            form.diagnostico_Kinestesico=resultados[2]
            form.save(update_fields=["diagnostico_Visual","diagnostico_Auditivo","diagnostico_Kinestesico"])
            print ("hecho estan guardados")
            
            return HttpResponseRedirect("/anexo13/gracias/")
        else:
            self.errores.append(form.errors)
            print ("No es valido el formulario")
            print(self.errores)
            return render(request, self.template_name, {'form': form})

def diagnosticoInventerioE(formulario):
    resultados=[0,0,0]
    form=formulario.__dict__
    for p,v in form.items():
        if p=='pregunta1' or p=='pregunta3' or p=='pregunta6' or p=='pregunta9'or p=='pregunta10' or p=='pregunta11' or p=='pregunta14':
            resultados[0]=resultados[0]+int(v)
        if p=='pregunta2' or p=='pregunta5' or p=='pregunta12' or p=='pregunta15'or p=='pregunta17' or p=='pregunta21' or p=='pregunta23':
            resultados[1]=resultados[1]+int(v)
        if p=='pregunta4' or p=='pregunta7' or p=='pregunta8' or p=='pregunta13'or p=='pregunta19' or p=='pregunta22' or p=='pregunta24':
            resultados[2]=resultados[2]+int(v)
    return resultados
def Contador(formulario):

    form=formulario.__dict__
    cont1=0
    num = 0
    for p,v in form.items():
        if v=='0' :
            num=num + 1
    return num

def valores(tipo,contador):
    calificacion=""
    lis2=[]
    datos=[[20,20,20,[57,60],8],
    [19,[18,19],19,[52,56],7],
    [18,17,18,[50,51],6],
    [[16,17],16,17,[48,49],5],
    [[14,15],[14,15],16,[43,47],4],
    [[12,13],13,15,[39,42],3],
    [11,12,[13,14],[37,38],2],
    [10,11,12,[34,36],1],
    [[0,9],[0,10],[0,11],[0,33],0]]

    for i in range(0,8):
        if type(datos[i][tipo]) is int:
            if contador==datos[i][tipo]:
                calificacion=datos[i][4]
        else:
            lis2=datos[i][tipo]
            if contador>=lis2[0] and contador<=lis2[1]:
                calificacion=datos[i][4]
    return calificacion

