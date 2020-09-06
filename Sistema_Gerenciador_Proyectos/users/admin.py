from django.contrib import admin
from .models import Proyecto, Usuario, Rol, Permiso, Tarea, LineaBase

# Register your models here.

admin.site.register(Proyecto)
admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Permiso)
admin.site.register(Tarea)
admin.site.register(LineaBase)