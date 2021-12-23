from django.shortcuts import render
from django.views import generic
from app_todo.models import TodoListItem
from app_todo.forms import ToDoForm


class ToDoListView(generic.ListView):
    model = TodoListItem
    template_name = 'app_todo/todo_list.html'
    context_object_name = 'todo_list'
    queryset = TodoListItem.objects.order_by('-date_publication')

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
            return render(request, 'app_todo/todo_list.html', {'form': form})
        else:
            form = ToDoForm()
            return render(request, 'app_todo/todo_list.html', {'form': form})
