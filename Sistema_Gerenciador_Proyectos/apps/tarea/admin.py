from django.contrib import admin
from apps.tarea.models import Tarea,Tarea_padre

# Register your models here.
admin.site.register(Tarea_padre)
admin.site.register(Tarea)