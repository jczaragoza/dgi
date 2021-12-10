from django.db import models
from persona.models import Persona

# Create your models here.
class Cursos(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, blank=True, null=True)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    horas = models.IntegerField(null=True, blank=True)
    tipo_curso = models.CharField(max_length=100, blank=True, null=True)
    #inicio_curso = models.DateTimeField(blank=True, null=True)
    #fin_curso = models.DateTimeField(blank=True, null=True)
    documento = models.CharField(max_length=20, blank=True, null=True)

    #def years(self):
    #    return self.fin_curso.year - self.inicio_curso.year
    #def meses(self):
    #    return self.fin_curso.month - self.inicio_curso.month
    #def dias(self):
    #    dif = self.fin_curso - self.inicio_curso
    #    return dif.days

    #def hours(self):
    #    a = self.inicio_curso
    #    b = self.fin_curso
    #    secs = (b-a).total_seconds()
    #    mins = secs/60
    #    hors = mins/60

    #   return hors

    def __str__(self):
        return self.nombre

    class Meta: 
        ordering = ['nombre']

