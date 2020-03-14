from django.contrib import admin
from .models import Proyecto, Usuario, Rol
# Register your models here.

admin.site.register(Proyecto)
admin.site.register(Usuario)
admin.site.register(Rol)
