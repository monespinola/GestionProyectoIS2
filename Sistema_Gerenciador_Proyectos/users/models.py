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

class Permiso(models.Model):
    nombre_permiso = models.CharField(max_length=50)
    descripcion = models.CharField(max_length = 200, help_text = "Ingrese descripcion")

    def __str__ (self):
            return '%s' % (self.nombre_permiso)

class Rol(models.Model):        
    # Campos
    nombre_rol = models.CharField(max_length = 30, help_text = "Ingrese el nombre del rol")
    descripcion = models.CharField(max_length = 200, help_text = "Ingrese descripcion")
    permiso = models.ManyToManyField(Permiso, help_text = "Seleccione uno o más permisos")

    def __str__(self):
        """Formato del rol por proyecto."""
        return '{0}'.format(self.nombre_rol)

    def get_absolute_url(self):
        """Retorna el URL para acceder a una instancia de un rol en particular."""
        return reverse('rol-detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
# Create your models here.
class Tarea(models.Model):
    version = models.CharField(max_length=50)
    prioridad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    observacion = models.CharField(max_length=50)
    id_tarea_padre = models.IntegerField()