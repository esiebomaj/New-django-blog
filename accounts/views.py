from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class CreateAccountView(CreateView):
	form_class=UserCreationForm
	template_name='accounts/signup.html'
	success_url=reverse_lazy('login')