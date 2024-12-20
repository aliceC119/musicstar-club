from django.test import TestCase

# Create your tests here.
from .forms import CommentForm


class TestCommentForm(TestCase):

    """Test for the 'comment' field"""
    def test_form_is_valid(self):
        
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid())
        
    def test_form_is_invalid(self):
          
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")