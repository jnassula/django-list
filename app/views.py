from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

def register_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('task_list')
    else:
        task_form = TaskForm()
    return render(request, 'form_register.html', {'task_form': task_form})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})