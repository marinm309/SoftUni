from django.db import models
import uuid
from users.models import Profile
from django.contrib.humanize.templatetags import humanize
from django.core.validators import FileExtensionValidator

class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    like = models.IntegerField(default=0, null=True)
    num_of_comments = models.IntegerField(default=0, null=True)
    photo = models.ImageField(null=True, upload_to='posts')
    file_upload = models.FileField(null=True, upload_to='posts', validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv','png','jpg'])])
    post_type = models.CharField(max_length=100, null=True)
    user_liked = models.ForeignKey('Likes', on_delete=models.SET_NULL, null=True)

    
    def get_date(self):
        return humanize.naturaltime(self.created)

    def num_of_posts(self, user):
        posts = Post.objects.filter(user = user)
        return len(posts)

    def num_of_likes(self):
        likes = Likes.objects.filter(post_liked = self)
        return len(likes)

    def num_of_comments(self):
        comments = Comments.objects.filter(post=self)
        return len(comments)

    def liked_by_user(self, request):
        user = request.user.profile
        liked = Likes.objects.filter(post_liked=self, user=user)
        return len(liked)

    def liked_by_user_home(self):
        liked = Likes.objects.filter(post_liked=self)
        return liked

    def __str__(self) -> str:
        return str(self.title)


class Comments(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    likes = models.IntegerField(default=0, null=True)
    user_liked = models.ForeignKey('CommentLikes', on_delete=models.SET_NULL, null=True)

    def num_of_likes(self):
        liked = CommentLikes.objects.filter(comment=self)
        return len(liked)

    def get_date(self):
        return humanize.naturaltime(self.created)

    def num_of_likes(self):
        likes = CommentLikes.objects.filter(comment=self)
        return len(likes)

    def __str__(self) -> str:
        return str(self.description)

class Likes(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    post_liked = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return str(self.id)

class CommentLikes(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey(Comments, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.comment)