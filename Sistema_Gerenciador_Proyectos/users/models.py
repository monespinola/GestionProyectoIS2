from django.db import models
from django.urls import reverse

# Create your models here.
class Usuario(models.Model):
	nombre = models.CharField(max_length = 50, help_text = "Ingrese el nombre del usuario")
	apellido = models.CharField(max_length = 50, help_text = "Ingrese el apellido del usuario")

	def __str__ (self):
		return '%s, %s' % (self.apellido, self.nombre)

	def get_absolute (self):
		return reverse ('usuario-detail', args = [str(self.id)])
