from django.shortcuts import render
from django.views import generic
from app_todo.models import TodoListItem
from app_todo.forms import ToDoForm
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView


class ToDoListView(generic.ListView):
    model = TodoListItem
    template_name = 'app_todo/todo_list.html'
    context_object_name = 'todo_list'
    queryset = TodoListItem.objects.order_by('date_due')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ToDoForm()
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = ToDoForm(request.POST)
        if form.is_valid():
            context = form.save(commit=False)
            context.save()
            return HttpResponseRedirect('/todo')
        else:
            form = ToDoForm()
            return render(request, 'app_todo/todo_list.html', {'form': form})


class ToDoDetailView(DetailView):
    model = TodoListItem
    template_name = 'app_todo/todo_detail.html'


class ToDoDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'app_todo.can_delete'
    model = TodoListItem
    template_name = 'app_todo/todo_delete.html'
    success_url = reverse_lazy('todo_list')
