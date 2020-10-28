from django.urls import path
from .views import PostsView, PostView

urlpatterns = [
    path('', PostsView.as_view(), name='home'), 
    path('post/<int:pk>', PostView.as_view(), name='post'),
]