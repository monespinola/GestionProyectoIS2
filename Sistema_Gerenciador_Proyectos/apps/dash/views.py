from django.shortcuts import render,redirect
from apps.tarea.models import Tarea
from apps.tarea.form import TareaForm
import sqlite3

# Create your views here.
def indexPage(request):
    # define connection and cursor

    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()

    # get results
    consulta="*"
    cursor.execute("SELECT "+ consulta +" FROM proyecto_proyecto")

    results = cursor.fetchall()
    cursor.close()
    connection.close()

    #var=['enero','febrero','marzo']
    var=[results[0][1],results[0][2]]
    print(var)
    context={'var':var}
    return render(request,'index.html',context)

def vista_lb(request):
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()

    # get results
    consulta="'lineabase',id,descripcion,estado,version"
    cursor.execute("SELECT "+ consulta +" FROM tarea_tarea")

    result = cursor.fetchall()
    cursor.close()
    connection.close()

    #var=['enero','febrero','marzo']
    #tareas=Tarea.objects.all()
    context={'var':result}
    return render(request,'vista_lb.html',context)

'''def tarea_view(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tarea:index')
    else:
        form = TareaForm()
    return render(request,'tarea/tarea_form.html',{'form':form})'''