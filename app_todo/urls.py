from django.urls import path
from app_todo.views import ToDoListView


urlpatterns = [
    path('', ToDoListView.as_view(), name='todo_list')
]