from django.shortcuts import render
from app_note.forms import CommentForm, UploadFileForm, DocumentForm, MultiFileForm, UploadNoteForm, NoteSearchForm
from app_note.models import Note, File
from django.views import generic
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django import forms
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.db.models import Q


'''
def sample_view(request):
    html = '<body><h1>Django sample_view</h1><br><p>Отладка sample_view</p></body>'
    return HttpResponse(html)
'''
class AboutView(TemplateView):

    template_name = "app_note/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['note_about'] = 'WebNote это веб блокнот.'
        return context



class NoteListView(generic.ListView):
    model = Note
    template_name = 'app_note/note_list.html'
    context_object_name = 'note_list'
    queryset = Note.objects.order_by('-date_publication')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = NoteSearchForm()
        context['form'] = form
        return context


class NoteDetailView(DetailView):
    model = Note

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CommentForm()
        if self.request.user.is_authenticated:
            form.fields['author'].widget = forms.HiddenInput()
            form.fields['author'].initial = self.request.user.username
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        note = self.get_object()
        if request.user.is_authenticated:
            user = request.user
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.note = note
                comment.author = user
                comment.user = user
                comment.save()
                return redirect('note_detail', pk=note.pk)
            else:
                form = CommentForm()
            return render(request, 'app_note/note_detail.html', {'form': form})
        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.note = note
                comment.author = comment.author + ' (Anonym)'
                comment.save()
                return redirect('note_detail', pk=note.pk)
            else:
                form = CommentForm()
            return render(request, 'app_note/note_detail.html', {'form': form})


class NoteCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'app_note.can_publish'
    model = Note
    template_name = 'app_note/note_add.html'
    fields = ['title', 'text']


class NoteUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'app_note.can_edit'
    model = Note
    template_name = 'app_note/note_edit.html'
    fields = ['title', 'text']


class NoteDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'app_note.can_delete'
    model = Note
    template_name = 'app_note/note_delete.html'
    success_url = reverse_lazy('note_list')


class NoteSearchView(generic.ListView):
    model = Note
    template_name = 'note_search.html'

    def get_queryset(self):
        form = NoteSearchForm(self.request.GET)
        if form.is_valid():
            serch_field = form.cleaned_data.get('search_field')
            object_list = Note.objects.filter(Q(title__icontains=serch_field) | Q(text__icontains=serch_field))
            return object_list


def upload_file(request):
    if request.method =='POST':
        upload_file_form = UploadFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            file = request.FILES['file']
            return HttpResponse(content=file.name, status=200)
    else:
        upload_file_form = UploadFileForm()

    context = {
        'form2': upload_file_form
    }
    return render(request, 'app_note/upload.html', context=context)




def form_upload(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method =='POST':
        form_upload = DocumentForm(request.POST, request.FILES)
        if form_upload.is_valid():
            file = form_upload.save(commit=False)
            file.note = note
            form_upload.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form_upload = DocumentForm()
    return render(request, 'app_note/form_upload.html', {
        'form_upload': form_upload
        })


def upload_files(request, pk):
    if request.user.is_authenticated:
        note = get_object_or_404(Note, pk=pk)
        if request.method =='POST':
            form = MultiFileForm(request.POST, request.FILES)
            if form.is_valid():
                files = request.FILES.getlist('file_field')
                for f in files:
                    instance = File(file=f)
                    instance.note = note
                    instance.save()
                return redirect('note_detail', pk=note.pk)
        else:
            form = MultiFileForm()
        return render(request, 'app_note/upload_files.html', {'form': form})
    else:
        return HttpResponse(content='Для загрузки файлов необходимо авторизоваться!', status=200)


def upload_note(request):
    if request.method == 'POST':
        form = UploadNoteForm(request.POST, request.FILES)
        if form.is_valid():
            price_file = form.cleaned_data['file'].read()
            price_str = price_file.decode('utf-8').split('\n')
            #csv_reader = reader(price_str, delimiter=",", quotechar='"')
            for row in price_str[: -1]:
                tmp = Note.objects.create()
                tmp.title = row.split(';')[0]
                tmp.text = row.split(';')[1]
                tmp.save()
            return HttpResponse(content='Новости были успешно загружены', status=200)
    else:
        form = UploadNoteForm()

        context = {
            'form': form
            }
    return render(request, 'app_note/upload.html', context)#было context=context вместо form: form  (поставил context вместо {'form': form})




'''
def add_comment_to_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = CommentForm()
    return render(request, 'app_news/add_comment_to_news.html', {'form': form})'''