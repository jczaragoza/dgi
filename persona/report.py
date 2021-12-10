#from config.wsgi import *
from django.http import response, HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.urls.base import reverse_lazy
#from weasyprint import HTML, CSS
from django.conf import settings
import os
from cursos.models import Cursos
from persona.models import *
from django.views.generic.base import TemplateView 

class ReportView(TemplateView):
    
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        try:
            template = get_template('persona/report.html')
            context = {
                'persona': Persona.objects.get(pk=self.kwargs['pk']),
                'cursos': Cursos.objects.filter(persona_id=pk),
            }
            html = template.render(context) 
            #Definiendo rutaestatica para estilo
            css_url = os.path.join(settings.BASE_DIR, 'static/assets/css/bootstrap.min.css')
            #Agregando css a html
            pdf = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(stylesheets=[CSS(css_url)])
            return HttpResponse(pdf, content_type='application/pdf')
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('index')) 
