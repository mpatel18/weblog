from django.urls import path
from .views import PostsView, PostView, NewPostView, UpdatePostView, DeletePostView, UserRegistration

urlpatterns = [
    path('', PostsView.as_view(), name='home'), 
    path('post/<int:pk>', PostView.as_view(), name='post'),
    path('new_post/', NewPostView.as_view(), name='new_post'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('register/', UserRegistration.as_view(), name='register'),
]