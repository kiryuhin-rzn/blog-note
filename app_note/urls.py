from django.urls import path
from . import views
from app_note.views import upload_note
from .views import NoteListView, NoteDetailView, NoteUpdateView, NoteCreateView, NoteDeleteView


urlpatterns = [
    path('', NoteListView.as_view(), name='note_list'),
    path('note/<int:pk>', NoteDetailView.as_view(), name='note_detail'),
    path('note/add/', NoteCreateView.as_view(), name='add_note'),
    path('note/<int:pk>/edit/', NoteUpdateView.as_view(), name='note_edit'),
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
    #path('post/<int:pk>/comment/', views.add_comment_to_note, name='add_comment_to_news'),
    path('note/upload/', views.upload_file, name='upload'),
    path('note/<int:pk>/upload_files/', views.upload_files, name='upload_files'),
    #path('news/uploads/', Rectangle, name='uploads'),
    path('note/uploads/', upload_note, name='uploads'),
    #path('news/<int:pk>/form_upload/', views.form_upload, name='form_upload'),
]