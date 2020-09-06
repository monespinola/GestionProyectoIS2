from django.db import models
from apps.tarea.models import Tarea

# Create your models here.
class Proyecto(models.Model):
    nombre_pro= models.CharField(max_length=50)
    descripcion_pro= models.CharField(max_length=50)
    tareas = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    #tarea1= Tarea.objects.filter(descripcion__icontains='tarea1')
    #campo_tarea=models.CharField(max_length=50,default=tarea1.descripcion)
    #nombre_pro.editable=False
    #descripcion_pro.editable=False
    def __str__(self):
        return '{}'.format(self.nombre_pro)