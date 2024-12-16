from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

# Create your views here.

class HomeView(generic.TemplateView):

    template_name = "gunnerdolist/index.html"



@login_required
def task_details(request):

    tasks = Task.objects.filter(user=request.user)
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.progress = 1
            task.save()
            return redirect('/')
    form = TaskForm()

    return render(request,
                  'gunnerdolist/taskpage.html', {'tasks': tasks, 'task_form': form, })

def update_task(request, pk):

    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.add_message(request, messages.SUCCESS, 'Task Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')
        return redirect('/')

    return render(request,
                  'gunnerdolist/update_task.html',
                  {'task_form': form, })


def delete_task(request, pk):

    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if task.user == request.user:
            task.delete()
            messages.add_message(request, messages.SUCCESS, 'Task deleted!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'You can only delete your own task!')
        return redirect('/')

    return render(request,
                  'gunnerdolist/delete_task.html',
                  {'task': task, })












