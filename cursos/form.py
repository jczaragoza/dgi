from django import forms
from django.forms import widgets
from cursos.models import *

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Layout, Submit, Row, Column
from crispy_forms.bootstrap import FormActions

class CursosForm(forms.ModelForm):
    
    class Meta:
        model = Cursos
        fields = '__all__'
    
    cursos_choices = [
        ('Diplomado', 'Diplomado'),
        ('Taller','Taller'),
        ('Curso','Curso'),
        ('Capacitación','Capacitación'),
    ]
    
    docs_choices = [
        ('Diploma', 'Diploma'),
        ('Constancia','Constancia'),
        ('Certificado','Certificado'),
    ]

    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    
    #persona = forms.MultipleChoiceField(required=False,
    #    widget=forms.CheckboxSelectMultiple,
    #    choices=FAVORITE_COLORS_CHOICES,)

    nombre = forms.CharField(label='Nombre de Curso', required=True)
    tipo_curso = forms.ChoiceField(label='Tipo de Curso', required=False, choices=cursos_choices)
    horas = forms.IntegerField(label='Total de Horas')
    #inicio_curso = forms.DateTimeField(label='Fecha de Nacimiento', widget=forms.TextInput(attrs={'type': 'datetime-local','class': 'form-control  datetimepicker'}), required=True)
    #fin_curso = forms.DateTimeField(label='Fin de Curso', widget=forms.TextInput(attrs={'type': 'datetime-local','class': 'form-control  datetimepicker'}), required=True ) 
    documento = forms.ChoiceField(label='Documento Obtenido', required=False, choices=docs_choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('persona', css_class='form-group col-md-6 mb-0'),
                Column('tipo_curso', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('nombre', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('horas', css_class='form-group col-md-6 mb-0'),
                
                css_class='form-row'
            ),
            Row(
                Column('documento', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            FormActions(
                Submit( 'save', 'Guardar', css_class = 'btn btn-primary' ),
                
            )
        )
