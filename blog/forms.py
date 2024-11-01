""" This module contains the form logic for creating posts. """

from .models import Comment
from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):

    """
    Allow superusers to use the form to create and publish posts.
    """

    class Meta:
        model = Post
        fields = ['title', 'featured_image', 'content', 'status', 'excerpt']
        widgets = {
            'content': SummernoteWidget(),

        }
    

class CommentForm(forms.ModelForm):

    """
    Allow all users to use the form to create and publish comments.
    """

    class Meta:
        model = Comment
        fields = ('body',)

        