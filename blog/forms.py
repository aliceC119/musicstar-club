from .models import Comment
from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'featured_image', 'content', 'status', 'excerpt']
        widgets = {
            'content': SummernoteWidget(), 
            
        }
    
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


        