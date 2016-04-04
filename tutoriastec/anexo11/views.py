from django.shortcuts import render
from  django.http  import  HttpResponseRedirect 
from  django.views.generic  import  View
from .forms import OrgEstudioForm
# Create your views here.

class OrgStudioView(View):
    Form= OrgEstudioForm
    initial=''