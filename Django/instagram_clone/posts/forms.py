from django.forms import ModelForm
from .models import Post, Comments


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['description']