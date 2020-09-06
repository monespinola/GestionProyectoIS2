from django import forms
from apps.tarea.models import Tarea

class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea

        fields =[
            'version',
            'prioridad',
            'estado',
            'descripcion',
            'observacion',
            'FK_id_tarea_padre',
        ]
        labels = {
            'version':'Version',
            'prioridad':'Prioridad',
            'estado':'Estado',
            'descripcion':'Descripcion',
            'observacion':'Observacion',
            'FK_id_tarea_padre':'FK_id_tarea_padre',
        }
        widgets = {
            'version': forms.TextInput(attrs={'class':'form-control'}),
            'prioridad': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'observacion': forms.TextInput(attrs={'class':'form-control'}),
            'FK_id_tarea_padre': forms.Select(attrs={'class':'form-control'}),
        }