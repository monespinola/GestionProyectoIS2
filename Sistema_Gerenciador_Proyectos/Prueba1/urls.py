"""Prueba1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Prueba1.views import vista1,countusergroup
from django.conf.urls import url
from apps.dash import views
#from apps.tarea.views import tarea_view

urlpatterns = [
    path('vista_lb/',views.vista_lb),
    path('index/',views.indexPage),
    path('admin/', admin.site.urls),
    path('vista1/', vista1),
    path('countusergroup/',countusergroup),
    #path(r'^nuevo$', tarea_view, name='index')
    
]
