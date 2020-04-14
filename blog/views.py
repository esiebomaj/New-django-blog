from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import post
from django.urls import reverse_lazy
# Create your views here.

class BlogListView(ListView):
		model=post

		template_name='blog/home.html'

class BlogDetailView(DetailView):
	model=post

	template_name='blog/post_detail.html'


class PostCreateView(CreateView):
	model=post
	template_name='blog/new_post.html'
	fields=['author', 'title', 'content']

class PostUpdateView(UpdateView):
	model=post
	template_name='blog/update_post.html'
	fields=['author', 'title', 'content']
	
class PostDeleteView(DeleteView):
	model=post
	template_name='blog/delete_Post.html'

	success_url=reverse_lazy('home')