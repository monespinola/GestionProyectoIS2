from django.db import models
from django.urls import reverse

# Create your models here.
class Usuario(models.Model):
	nombre = models.CharField(max_length = 50, help_text = "Ingrese el nombre del usuario")
	apellido = models.CharField(max_length = 50, help_text = "Ingrese el apellido del usuario")

	def __str__ (self):
		return '%s, %s' % (self.apellido, self.nombre)

    def get_absolute_url(self):
        return reverse('usuario-detail', args=[str(self.id)])

class Proyecto(models.Model):
    """
    Una clase típica definiendo un modelo, derivado desde la clase Model.
    """
    # Campos
    nombre_proyecto = models.CharField(max_length = 50, help_text="Ingrese el nombre del proyecto")
    descripcion= models.CharField(max_length = 200, help_text="Descripción del proyecto")

    estados_proyecto = (
    	('a','Activo'),
    	('i','Inactivo'),
    	('f','Finalizado'),
    )

    estado = models.CharField(
        max_length = 1,
        choices = estados_proyecto,
        blank = True,
        default = 'a',
        help_text = "Estados del proyecto"
    )

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Proyecto
        """
        return reverse('proyecto-detail', args=[str(self.id)])

    def __str__ (self):
		return '%s, %s' % (self.nombre_proyecto, self.estados_proyecto)

    # Metadata
    class Meta: 
        ordering = ["estado"]