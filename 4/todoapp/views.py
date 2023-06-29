from django.shortcuts import render
from django.views import View
from .models import ToDoItem
# Create your views here.

class HomeToDoListView(View):
    
    def get(self, request):
        todos = ToDoItem.objects.all()
        context = {
            'todos': todos
        }
        return render(request, 'home.html', context)