from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from webapp.models import Task
from webapp.forms import TaskForm

class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'create_task.html'
    success_url = reverse_lazy('index')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'edit_task.html'
    success_url = reverse_lazy('index')

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('index')

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail_task.html'
    success_url = reverse_lazy('index')