from django.shortcuts import redirect, render
from .models import Todo
from .form  import Todoinfo
# Create your views here.
def viewTodo(request):
    todos = Todo.objects.all()

    if request.method == 'POST':
        form = Todoinfo(request.POST)
        if form.is_valid():
            form.save()
           
    else:
        form = Todoinfo()

    return render(request, 'index.html', {'todo': todos, 'form': form})
def edit(request,pk):
    
    instance_to_be_edited = Todo.objects.get(pk=pk)

    if request.method == 'POST':
        form = Todoinfo(request.POST, instance=instance_to_be_edited)
        if form.is_valid():
            form.save()
    else:
        form = Todoinfo(instance=instance_to_be_edited)

    return render(request, 'edit.html', {'form': form})
def delete(request,pk):
    try:
        instance_to_be_deleted = Todo.objects.get(pk=pk)
        instance_to_be_deleted.delete()
        todolist = Todo.objects.all()
        return redirect(request.path)
    except Todo.DoesNotExist:
        # Render a custom error page
        return redirect('home')