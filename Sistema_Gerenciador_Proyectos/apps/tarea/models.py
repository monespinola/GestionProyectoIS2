from django.db import models
#from apps.proyecto.models import Proyecto

# Create your models here.
class Tarea_padre(models.Model):
    version = models.CharField(max_length=50)
    prioridad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    observacion = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.descripcion)
class Tarea(models.Model):
    version = models.CharField(max_length=50)
    prioridad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    observacion = models.CharField(max_length=50)
    FK_id_tarea_padre = models.OneToOneField(Tarea_padre,on_delete=models.CASCADE)
    #id_tarea_padre = models.OneToOneField(Tarea,on_delete=models.CASCADE,primary_key=True)
    #id_tarea_padre = models.ManyToManyField(to='Tarea')

    def __str__(self):
        return '{}'.format(self.descripcion)
