from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
#from django.utils.translation import gettext_lazy as _


class Note(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    title = models.CharField(max_length=1000, db_index=True, verbose_name='title')
    text = models.TextField(verbose_name='text')
    author = models.CharField(max_length=200)
    date_publication = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    tag = models.ManyToManyField('Tag', default=None, blank=True)

    class Meta:
        verbose_name = 'note'
        verbose_name_plural = 'notes'
        permissions = (
            ('can_publish', 'Может публиковать'),
            ('can_edit', 'Может редактировать'),
            )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note_detail', args=[str(self.id)])


class Comment(models.Model):
    STATUS_CHOICES = (
    ('d', 'Dell'),
    ('p', 'Published'),
    )
    note = models.ForeignKey('Note', default=None, null=True, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return f'{self.text}'[0:15]+'...'


class Tag(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class File(models.Model):
    file = models.FileField(upload_to='files/')
    description = models.TextField(blank=True)
    created_ad = models.DateTimeField(auto_now_add=True)
    note = models.ForeignKey('Note', default=None, on_delete=models.CASCADE, related_name='file')