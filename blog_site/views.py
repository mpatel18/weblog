from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.

class PostsView(ListView):
    model = Post
    template_name = "home.html"

class PostView(DetailView):
    model = Post
    template_name = "post.html"

class NewPostView(CreateView):
    model = Post
    template_name = "new_post.html"
    fields = "__all__"

