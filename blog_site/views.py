from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class PostsView(ListView):
    model = Post
    template_name = "home.html"

class PostView(DetailView):
    model = Post
    template_name = "post.html"

