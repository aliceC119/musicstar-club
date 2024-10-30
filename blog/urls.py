""" This module contains the URL pattern for the Blog app. """

from . import views
from django.urls import path, include
from .views import create_post

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/', views.create_post, name='create_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete, name='comment_delete'),
    path('approve_comment/<int:comment_id>/', views.approve_comment, name='approve_comment'),
    path('summernote/', include('django_summernote.urls')),
]
