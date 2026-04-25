from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
from .forms import TaskForm, ProjectForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def hello(request, username:str):
    return HttpResponse("<h1>Hello %s</h1>" %username)

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html', {'projects': projects})

def task(request, idTask:int):
    task = get_object_or_404(Task, id=idTask)
    return render(request, 'task.html', {'task': task})

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TaskForm()
        })
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                Task.objects.create(
                    title=form.cleaned_data['title'],
                    description=form.cleaned_data['description'],
                    project_id=1
                )
                return redirect('/task/' + str(Task.objects.last().id))
            except Exception as e:
                return JsonResponse({
                    'message': 'Error creating task',
                    'error': str(e)
                }, status=500)
    else:
        return JsonResponse({
            'message': 'Method not allowed'
        }, status=405)

def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html', {
            'form': ProjectForm()
        })
    elif request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            try:
                Project.objects.create(
                    name=form.cleaned_data['name'],
                    description=form.cleaned_data['description']
                    
                )
                return redirect('projects')
            except Exception as e:
                return JsonResponse({
                    'message': 'Error creating project',
                    'error': str(e)
                }, status=500)
    else:
        return JsonResponse({
            'message': 'Method not allowed'
        }, status=405)