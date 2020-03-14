from django.db import models
class Proyecto(models.Model):
    """
    Una clase típica definiendo un modelo, derivado desde la clase Model.
    """
    # Campos
    nombre_proyecto = models.CharField(max_length=50, help_text="Ingrese el nombre del proyecto")
    descripción= models.CharField(max_length=90, help_text="Descripción del proyecto")
    
    estados_proyecto= (('a','Activo'),
    ('i','Inactivo'),
    ('f','Finalizado'), )
    estado= models.CharField(
        max_length=1,
        choices= estados_proyecto,
        blank= True,
        default= 'a',
        help_text= 'Estados del proyecto'
    )
     def get_absolute_url(self):
        """Retorna el URL para acceder a una instancia del proyecto en particular."""
        return reverse('proyecto-detail', args=[str(self.id)])

    def __str__(self):
        """Formato de nombre y estado del proyecto."""
        return '{0}, {1}'.format(self.nombre_proyecto, self.estado)
    
    # Metadata
    class Meta: 
        ordering = ["estado"]

        




>>>>>>> Stashed changes
