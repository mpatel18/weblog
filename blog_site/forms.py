from django import forms
from .models import Post

class Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'length'}),
            'title_tag': forms.TextInput(attrs={'class': 'length'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'length'}),
            'title_tag': forms.TextInput(attrs={'class': 'length'}),
        }