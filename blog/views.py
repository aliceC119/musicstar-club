""" This module contains the views for the Blog app. """

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from .forms import PostForm
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.


class PostList(generic.ListView):

    """
    Display up to 6 published blog posts in every blog page.

    """

    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    """
    Set the logic of likes in posts.
    """

    liked = False

    if request.method == "POST":

        if request.method == "POST":

            if request.user.is_authenticated:
                user = request.user

                if post.likes.filter(id=user.id).exists():
                    post.likes.remove(user)
                    liked = False

                else:
                    post.likes.add(user)
                    liked = True
        """
        A message of 'Comment submitted and awiting approval'
        will be displayed when a user submitted a comment in a post.

        Renders the page on the blog/post_detail.html template.
        """

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "liked": liked,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def create_post(request):

    """
    Set a logic to Superuser to create posts on the frontend.

    Renders the page on the blog/create_post.html template when the superuser
    goes to the link in the home page.

    When the post is successfully created and published, renders the page
    on the blog/posting_success.html template.
    """
    if request.user.is_superuser:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('home')
        else:
            form = PostForm()
        return render(request, 'blog/create_post.html', {'form': form})
    else:
        # return redirect('post_list')  # Redirect non-superusers
        return redirect('home')  # Redirect non-superusers


def posting_success(request):
    return render(request, 'blog/posting_success.html')

    """
    Set the logic for the superusers to approve the comments on the frontend.
    """


@staff_member_required
def approve_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.approved = True
    comment.save()
    return redirect('home')