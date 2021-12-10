from typing import List
from django.forms.widgets import SelectDateWidget
from django.http import HttpResponseRedirect, request, HttpResponse, FileResponse, response

# QUERY
from django.db.models.query_utils import Q
from django.db.models import Count

#VISTAS GENÉRICAS
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

#LOGIN LOGOUT
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#SHORTCUTS
from django.shortcuts import render, redirect, get_object_or_404

#FORM
from .form import PersonaForm
from cursos.form import CursosForm

#Models
from persona.models import *
from cursos.models import *

def PersonaSearchView(request): 
    if request.method == 'POST':
        busqueda = request.POST['busqueda']
        
        resultado = Persona.objects.filter(
            Q(nombre__contains = busqueda) |
            Q(apaterno__contains = busqueda) |
            Q(amaterno__contains = busqueda) |
            Q(cuip__contains=busqueda) |
            Q(rfc__icontains=busqueda) |
            Q(curp__icontains=busqueda) |
            Q(clavesp__contains = busqueda)
        )
        return render(request,
        'persona/persona_search.html',
        {'busqueda' :busqueda,
        'resultado':resultado,
        })
    else:
        return render(request,
            'persona/persona_search.html',
            {}
        )

class PersonaList(LoginRequiredMixin, ListView):
    
    model = Persona
    paginate_by = 10  # if pagination is desired
    context_object_name = 'persona'

    def get_context_data(self, **kwargs):
                
        context = super(PersonaList, self).get_context_data(**kwargs)
        context['activo'] = Persona.objects.filter(estatus = 'Activo')
        
        return context

    

class PersonaCreate(LoginRequiredMixin, CreateView):
    """Persona create view"""
    model = Persona
    template_name = 'persona/persona_create.html'
    form_class = PersonaForm
    success_url = reverse_lazy('index')

           
class PersonaDetailView(LoginRequiredMixin, DetailView):
    template_name = 'persona/persona_detail.html'
    queryset = Persona.objects.all()
    context_object_name = 'persona'

    def get_context_data(self, *args, **kwargs):
        # El pk que pasas a la URL
        pk = self.kwargs.get('pk')
        context = super(PersonaDetailView, self).get_context_data(**kwargs)
        context['cursos'] = Cursos.objects.filter(persona_id=pk)
        return context

class PersonaUpdateView(LoginRequiredMixin, UpdateView): 
    """Update PErsona"""
    template_name = 'persona/persona_update.html'
    model = Persona
    form_class = PersonaForm
    context_object_name = 'persona' 
    success_url = reverse_lazy('index')
    

class PersonaDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'persona/persona_delete.html'
    model = Persona
    success_url = reverse_lazy('index')

         
def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid username and password'})

    return render(request, 'registration/login.html')


@login_required
def logout_view(request):
    """Logout"""
    logout(request)
    return redirect('logout')
    

class UiipView(LoginRequiredMixin, ListView): 
    template_name = 'persona/uiip_list.html' 
    paginate_by = 10

    queryset = Persona.objects.filter(adscripcion_id = 1)
    context_object_name = 'uiip'

class c5View(LoginRequiredMixin, ListView): 
    template_name = 'persona/c5_list.html' 
    paginate_by = 10

    queryset = Persona.objects.filter(adscripcion_id = 2)
    context_object_name = 'c5'

class uacView(LoginRequiredMixin, ListView):
    context_object_name = 'uac'
    paginate_by = 10 # add this
    
    queryset = Persona.objects.filter(adscripcion_id = 3)
    template_name = 'persona/uac_list.html'


    