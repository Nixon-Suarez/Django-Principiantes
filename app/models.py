from django.db import models
from datetime import date, timedelta

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(default=date.today())
    end_date = models.DateField(default=date.today() + timedelta(days=365))

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # en caso de eliminar un proyecto, se eliminan sus tareas asociadas
    estado = models.BooleanField(default=False)