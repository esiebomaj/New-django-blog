from django.contrib import admin
from django.urls import path, include
from .views import BlogListView, BlogDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib.auth import urls



urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post', BlogListView.as_view(), name='home'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='post-detail'),
    path('post/new', PostCreateView.as_view(), name='new-post'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    

]
