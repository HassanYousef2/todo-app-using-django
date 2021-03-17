from django.shortcuts import redirect, render

# Create your views here.




tasks = []

def addTask(request):
    
    if request.POST.get("task") :
        tasks.append(request.POST["task"])
        return redirect(viewTask)

    return render(request, 'todo/add.html')

def viewTask(request):


    return render(request, 'todo/view.html', {"tasks":tasks})

def deleteTask(request):
    if request.POST.get("task"):
        tasks.remove(request.POST["task"])
        return redirect(viewTask)

    return render(request, 'todo/delete.html', {"tasks":tasks})
