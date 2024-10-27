from .models import Comment
from django import forms
from .models import Post



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'featured_image', 'content', 'status', 'excerpt']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)