from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from todolist.models import Task
from todolist.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def home(request):
    context={
        'page':"Home Page from views.py"
    }
    
    return render(request, 'main.html', context)

@login_required
def todolist(request):

    if request.method == "POST":
        form_data = TaskForm(request.POST or None)
        if form_data.is_valid():
            instance = form_data.save(commit=False)
            instance.owner = request.user
            instance.save()
            messages.success(request,"Task Added Successfully.")
            return redirect("todolist")
        messages.success(request,"Something wENT WRONG.")

    all_tasks = Task.objects.filter(owner=request.user)
    paginator = Paginator(all_tasks, 4)
    page = request.GET.get("page")
    all_tasks = paginator.get_page(page)

    context={
        'all_tasks':all_tasks
    }
    return render(request, 'todolist.html', context)

@login_required
def delete_task(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    if task_obj.owner == request.user:
        task_obj.delete()
        messages.success(request, f"Task - {task_obj.task} Deleted.")
    else:
        messages.success(request, f"You are not allowed to Delete This")
    return redirect("todolist")

@login_required
def edit_task(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    
    if request.method == "POST":
        form_data = TaskForm(request.POST, None, instance=task_obj)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Task Updated Successfully.")
            return redirect("todolist")
        messages.success(request,"Error while Updating")
    else:
        context={
            'task_obj':task_obj
        }
        
        return render(request, 'edit_task.html', context)

@login_required
def complete_task(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    if task_obj.owner == request.user:
        task_obj.is_completed = True
        task_obj.save()
        messages.success(request,"Status changed to - 'Completed'")
        
    else:
        messages.success(request,"You are not allowed to change status")
    return redirect('todolist')
@login_required
def pending_task(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    if task_obj.owner == request.user:
        task_obj.is_completed = False
        task_obj.save()
        messages.success(request,"Status changed to - 'Pending'")
        
    else:
        messages.success(request,"You are not allowed to Change Status")
    return redirect('todolist')

def contact(request):
    
    return render(request, 'contact.html')

def aboutus(request):
    
    return render(request, 'aboutus.html')