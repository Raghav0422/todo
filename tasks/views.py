from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
from .forms import TaskForm

# Create your views here.

def index(request):
    tasks= Task.objects.all()
    form=TaskForm() #getting details from froms.py folder

    #in below function we are just checking data recieve from html front end via post method
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
                                            # redirecting to page of same view where this is getting posted    
        return redirect('/todo/tasks/')     # basically it is like after successful submition i have to show something
                                            # so i am redirecting to same page again 

    context = {'tasks':tasks, 'form':form}
    return render(request, 'list.html', context)
    #return HttpResponse("Hello World")

def updatetask(request,pk):
    task=Task.objects.get(id=pk)
    form= TaskForm(instance=task)

    if request.method =="POST":
        form = TaskForm(request.POST, instance= task )

        if form.is_valid():
            form.save()
            return redirect('/todo/tasks/')
    context ={'form':form}

    return render(request,"update_task.html",context)

def delete(request,pk):
    item = Task.objects.get(id=pk)

    if request.method=="POST":
        item.delete()
        return redirect('/todo/tasks/')

    context={'item':item}

    return render(request,"delete.html", context)