#VISTAS GENÉRICAS
from typing import List
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
#FORM
from cursos.form import CursosForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

#Models
from cursos.models import *
from persona.models import *

# Create your views here.

class CursoCreateView(LoginRequiredMixin, CreateView):
    """Cursos create view"""
    model = Cursos
    template_name = 'cursos/curso_create.html'
    form_class = CursosForm
    success_url = reverse_lazy('index')


#DATATABLE


def category_list(request):
    data = {
        'title': 'Listado de Cursos',
        'categories': Cursos.objects.all()
    }
    return render(request, 'cursos/list.html', data)


class CursoListView(ListView):
    model = Cursos
    template_name = 'cursos/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Cursos'
        return context



"""class CursoListView(LoginRequiredMixin, ListView): 
    model = Cursos
    context_object_name = 'cursos'
    paginate_by = 10
    queryset = Cursos.objects.all()
    template_name = 'cursos/cursos_list.html' 
"""    
class CursoUpdateView(LoginRequiredMixin, UpdateView): 
    """Update Curso"""
    template_name = 'cursos/curso_update.html'
    model = Cursos
    form_class = CursosForm
    context_object_name = 'curso' 
    success_url = reverse_lazy('index')


class CursoDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'cursos/cursos_delete.html'
    model = Cursos
    success_url = reverse_lazy('index')


      
def showlist(request):
    results = Persona.objects.all()
    return render(request, "cursos/search_curso.html", {"showcurso":results})
