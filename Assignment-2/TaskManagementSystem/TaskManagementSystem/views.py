from django.shortcuts import render
from task.models import TaskModel

def home(request):
    return render(request, 'home.html')

def show_task(request):
    data=TaskModel.objects.all()
    return render(request, 'show_task.html',{'data':data})