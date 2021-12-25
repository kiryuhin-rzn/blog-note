from django import forms
from app_todo.models import TodoListItem


class ToDoForm(forms.ModelForm):

    class Meta:
        model = TodoListItem
        fields = ('content', 'date_due')

        labels = {
            'date_due': ('гггг-мм-дд'),
        }
