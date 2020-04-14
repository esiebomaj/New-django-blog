from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import urls
from accounts.views import CreateAccountView

urlpatterns = [
    path('accounts', include(urls)),
    path('signup', CreateAccountView.as_view(), name='signup'),
    
]
