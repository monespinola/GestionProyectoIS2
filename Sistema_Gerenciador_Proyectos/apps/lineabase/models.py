from django.db import models
from apps.tarea.models import Tarea

# Create your models here.
class Lineabase(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    tareas =models.ForeignKey(Tarea,on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre)