#VISTAS GENÉRICAS

from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateResponseMixin, TemplateView, View 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


#FORM


#Models
from persona.models import Persona

def index(request):
    total=Persona.objects.filter(estatus = 'Activo').count()
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'persona/dashboard.html',
        context1={'total':total},
    )
