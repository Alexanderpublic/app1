#-*- coding: utf-8 -*-

from django.forms import ModelForm
from models import Comment

class CommentForm(ModelForm):
    class Meta():
        model = Comment
        fields = ['comment_text']