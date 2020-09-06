from django.db import models

# Create your models here.
class Permiso(models.Model):
    nombre= models.CharField(max_length=50)
    LOAN_STATUS = (
        ('crearproyecto', 'crearproyecto'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    permisos = models.CharField(max_length=50, choices=LOAN_STATUS, blank=True, default='crearproyecto', help_text='acciones que se le permitiran')
    Lista_permisos  =  models.ManyToManyField ( 'descripcion' )

class descripcion(models.Model):
    nombre= models.CharField(max_length=50)
