""" This module contains the database models for the blog app. """

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

# Create your models here.

# A tuple to hold the status key for the Blog model.
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """

    The Model for the creating a post on the Blog app.



    Admin or supersuers are needed to fill in all the fields listed below in

    order to create a post and publish it in the administration panel or

    on the frontend.

    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='post')

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return
        f"The title of this post is {self.title}| written by { self.author}"

    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)


class Comment(models.Model):

    """

    The Model of creating comment for the posts in the Blog app.

    Logged-in users can create comments. Admin or the superusers

    have a choice to choose approve or not approve the comments.

    A date of the comment will be displayed after it is submitted.

    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


class SocialPost(models.Model):
    """

    The Model of creating a post when it is shared on the social media

    platform. The fields listed below will be displayed along with the post

    once it is shared to the social media platform.

    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField \
    (upload_to='posts/%Y/%m/%d/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:50]

    class Meta:
        ordering = ['-created_at']