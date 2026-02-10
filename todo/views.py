from django.shortcuts import render, redirect, get_object_or_404
from todo.models import Task

def addTask(request):
    if request.method == 'POST':
        task_text = request.POST.get('task')
        if task_text:
            Task.objects.create(task=task_text)
    return redirect('home')


def markComplete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = True
    task.save()
    return redirect('home')


def markUndone(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = False
    task.save()
    return redirect('home')


def deleteTask(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')


def editTask(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task_text = request.POST.get('task')
        if task_text:
            task.task = task_text
            task.save()
            return redirect('home')

    return render(request, 'edit_task.html', {'task': task})