from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, help_text="Enter a Title")
    title_tag = models.CharField(max_length=255, help_text='Enter a Tag for your Post')
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    class Meta:
       ordering = ['-date_added']

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('post', args=(str(self.pk)))
