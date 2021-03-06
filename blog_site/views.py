from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .models import Post
from .forms import Form, RegisterForm, LoginForm


# Create your views here.

class PostsView(ListView):
    model = Post
    template_name = "home.html"

class PostView(DetailView):
    model = Post
    template_name = "post.html"

class NewPostView(CreateView):
    model = Post
    form_class = Form
    template_name = "new_post.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePostView(UpdateView):
    model = Post
    form_class = Form
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = "confirm_delete_post.html"
    success_url = reverse_lazy('home')

class UserRegistration(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'

