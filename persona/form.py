from django import forms
from persona.models import Persona
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Layout, Submit, Row, Column


class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = '__all__'

    estatus_choices = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    tipo_sangre_choices = [
        ('O-','O-'),
        ('O+','O+'),
        ('A-','A-'),
        ('A+','A+'),
        ('B-','B-'),
        ('B+','B+'),
        ('AB-','AB-'),
        ('AB+','AB+'),
    ]

    clavesp = forms.CharField(label='Clave de Servidor Público', required=True)
    rfc = forms.CharField(label='RFC', required=True)
    apaterno = forms.CharField(label='Apellido Paterno', required=True)
    amaterno = forms.CharField(label='Apellido Materno', required=True)
    nombre = forms.CharField(label='Nombre(s)', required=True)
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento', widget=forms.TextInput(attrs={'type': 'date','class': 'form-control  datetimepicker'}), required=True)
    fecha_alta = forms.DateField(label='Fecha de alta', widget=forms.TextInput(attrs={'type': 'date','class': 'form-control  datetimepicker'}), required=False)
    estatus = forms.ChoiceField(label='Estatus', required=False, choices=estatus_choices, widget=forms.RadioSelect)
    foto = forms.ImageField(label='Foto',required=False)
    num_plaza = forms.CharField(label='Número de Plaza', required=False)
    cuip = forms.CharField(label='CUIP', required=False)
    curp = forms.CharField(label='CURP', required=False)

    calle = forms.CharField(label='Calle', required=False)
    interior = forms.CharField(label='Número Interior', required=False)
    exterior = forms.CharField(label='Número Exterior', required=False)
    cp = forms.CharField(label='Código Postal', required=False)
    correo = forms.EmailField(label='Correo Electrónico', required=False)
    telefono_fijo = forms.CharField(label='Teléfono Fijo', required=False)
    telefono_movil = forms.CharField(label='Teléfono Móvil', required=False)
    contacto_familiar = forms.CharField(label='Contacto Familiar', required=False)
    nss = forms.CharField(label='Clave ISSEMYM', required=False)
    tipo_sangre = forms.ChoiceField(label='Tipo de Sangre', required=False, choices=tipo_sangre_choices)
    fecha_baja = forms.DateField(label='Fecha de Baja', widget=forms.TextInput(attrs={'type': 'date','class': 'form-control  datetimepicker'}), required=False)
    motivo_baja = forms.CharField(label='Motivo de Baja', required=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('apaterno', css_class='form-group col-md-3 mb-0'),
                Column('amaterno', css_class='form-group col-md-3 mb-0'),
                Column('nombre', css_class='form-group col-md-3 mb-0'),
                Column('fecha_nacimiento', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('clavesp', css_class='form-group col-md-3 mb-0'),
                Column('rfc', css_class='form-group col-md-3 mb-0'),
                Column('cuip', css_class='form-group col-md-3 mb-0'),  
                Column('curp', css_class='form-group col-md-3 mb-0'),          
                css_class='form-row'
            ),
            Row(
                Column('num_plaza', css_class='form-group col-md-3 mb-0'),
                Column('fecha_alta', css_class='form-group col-md-3 mb-0'),
                Column('puesto', css_class='form-group col-md-3 mb-0'),
                Column('estatus', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('unidad_administrativa', css_class='form-group col-md-4 mb-0'),
                Column('adscripcion', css_class='form-group col-md-8 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('direccion', css_class='form-group col-md-6 mb-0'),
                Column('subdireccion', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('departamento', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('calle', css_class='form-group col-md-4 mb-0'),
                Column('interior', css_class='form-group col-md-4 mb-0'),
                Column('exterior', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('municipio', css_class='form-group col-md-4 mb-0'),
                Column('colonia', css_class='form-group col-md-4 mb-0'),
                Column('cp', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('correo', css_class='form-group col-md-4 mb-0'),
                Column('telefono_fijo', css_class='form-group col-md-4 mb-0'),
                Column('telefono_movil', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('contacto_familiar', css_class='form-group col-md-4 mb-0'),
                Column('nss', css_class='form-group col-md-4 mb-0'),
                Column('tipo_sangre', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('escolaridad', css_class='form-group col-md-4 mb-0'),
                Column('fecha_baja', css_class='form-group col-md-4 mb-0'),
                Column('motivo_baja', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('observaciones', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('foto', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Guardar', css_class='btn btn-secondary btn-round'),
            
        )


   