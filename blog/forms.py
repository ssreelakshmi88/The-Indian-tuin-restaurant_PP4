from .models import Comment
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget
from .models import Post, Comment
from django import forms



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)