from django.shortcuts import render, redirect
from django.views import View
from .models import ToDoItem
from .forms import ToDoCreateForm
from django.contrib import messages
# Create your views here.

class HomeToDoListView(View):
    
    def get(self, request):
        todos = ToDoItem.objects.all()
        context = {
            'todos': todos
        }
        return render(request, 'todoapp/home.html', context)
    
class CreateToDoView(View):
    
    form_class = ToDoCreateForm()
    
    def get(self, request):
        my_form = self.form_class()
        return render(request, 'todoapp/todo-create.html', {'form': my_form})
    
    def post(self, request):
        my_form = self.form_class(request.POST)
        if my_form.is_valid():
            new_todo = my_form.save()
            messages.add_message(request, messages.SUCCESS, f"{new_todo.title} task created!")
            return redirect('home')
        return render(request, 'todoapp/todo-create.html', {'form': my_form})