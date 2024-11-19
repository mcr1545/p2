from django.views.generic import ListView, CreateView
from .models import Todo

class TodoListView(ListView):
    model = Todo
    template_name = 'todo_list.html'

class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo_form.html'
    fields = ['title', 'description']
