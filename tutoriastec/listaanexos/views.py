from django.shortcuts import render

# Create your views here.
def listaanexos(request):
    return render(request,"anexos/anexos.html", {"mensaje":""})

