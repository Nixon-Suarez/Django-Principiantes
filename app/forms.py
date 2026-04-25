from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=100)
    description = forms.CharField(label="Descripcion", widget=forms.Textarea, required=False)

class ProjectForm(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=100)
    description = forms.CharField(label="Descripcion", widget=forms.Textarea, required=False)