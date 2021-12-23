from django.db import models


class TodoListItem(models.Model):
    content = models.TextField()
    date_publication = models.DateField(auto_now_add=True)
    date_due = models.DateTimeField(blank=True)
