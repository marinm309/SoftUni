from django.forms import ModelForm
from .models import Post, Comments


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'photo', 'description']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['description']