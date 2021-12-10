from django.db import models
from datetime import date
from smart_selects.db_fields import ChainedForeignKey


#Models combo Unidad ADministrativa
class Unidad_administrativa(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Adscripcion(models.Model):
    unidad_administrativa = models.ForeignKey(Unidad_administrativa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Direccion(models.Model):
    adscripcion = models.ForeignKey(Adscripcion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Subdireccion(models.Model):
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    subdireccion = models.ForeignKey(Subdireccion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre 

#Model Colonias

class Municipio(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre 

class Colonia(models.Model):
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre 

class Puesto(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    codigo_puesto = models.CharField(max_length=255, blank=True, null=True)
    nivel_rango = models.CharField(max_length=255, null=True, blank=True)
    sueldo_bruto = models.CharField(max_length=20,null=True, blank=True)
    sueldo_neto = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nombre 

# Create your model Persona here.
class Persona(models.Model): 

    clavesp = models.CharField(max_length=20, blank=True, null=True)
    rfc = models.CharField(max_length=13, blank=True, null=True)
    apaterno = models.CharField(max_length=255)
    amaterno = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    fecha_alta = models.DateField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    estatus = models.CharField(max_length=10, blank=True, null=True)
    foto = models.ImageField(blank=True, null=True, upload_to='persona/fotos')
    num_plaza = models.CharField(max_length=20, blank=True, null=True)
    cuip = models.CharField(max_length=20, null=True, blank=True)
    curp = models.CharField(max_length=18, null=True, blank=True)
    puesto = models.ForeignKey(Puesto, on_delete=models.SET_NULL, blank=True, null=True)
    unidad_administrativa = models.ForeignKey(Unidad_administrativa, on_delete=models.SET_NULL, blank=True, null=True)
    adscripcion = ChainedForeignKey(
        Adscripcion,
        on_delete=models.SET_NULL,
        chained_field="unidad_administrativa",
        chained_model_field="unidad_administrativa",
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True,
        null=True
    )
    direccion = ChainedForeignKey(
        Direccion,
        on_delete=models.SET_NULL,
        chained_field="adscripcion",
        chained_model_field="adscripcion",
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True,
        null=True

    )
    subdireccion = ChainedForeignKey(
        Subdireccion,
        on_delete=models.SET_NULL,
        chained_field="direccion",
        chained_model_field="direccion",
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True,
        null=True
    )
    departamento = ChainedForeignKey(
        Departamento,
        on_delete= models.SET_NULL,
        chained_field="subdireccion",
        chained_model_field="subdireccion",
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True,
        null=True
        
    )

    calle = models.CharField(max_length=255, null=True, blank=True)
    interior = models.CharField(max_length=10, null=True, blank=True)
    exterior = models.CharField(max_length=10, null=True, blank=True)
    municipio =models.ForeignKey(Municipio, on_delete=models.SET_NULL, blank=True, null=True)
    colonia = ChainedForeignKey(
        Colonia,
        chained_field="municipio",
        chained_model_field="municipio", 
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True,
        null=True
    )
    cp = models.CharField(max_length=5, blank=True, null=True)
    correo = models.EmailField(max_length=50, blank=True, null=True)
    telefono_fijo = models.CharField(max_length=20, blank=True, null=True)
    telefono_movil = models.CharField(max_length=20, blank=True, null=True)
    contacto_familiar = models.CharField(max_length=255, blank=True, null=True)
    nss = models.CharField(max_length=10, null=True, blank=True)
    tipo_sangre = models.CharField(max_length=5, null=True, blank=True) 
    escolaridad = models.CharField(max_length=255, null=True, blank=True)
    observaciones = models.CharField(max_length=255, null=True, blank=True)
    fecha_baja = models.DateField(null=True, blank=True)
    motivo_baja = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    #EDAD
    def edad(self):
        return date.today().year - self.fecha_nacimiento.year

    def __str__(self):
        return "%s %s %s" %(self.apaterno, self.amaterno, self.nombre) 
    
    class Meta: 
        ordering = ['created']

