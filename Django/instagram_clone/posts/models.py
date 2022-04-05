from django.db import models
import uuid
from users.models import Profile

class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    like = models.IntegerField(default=0, null=True)

    def __str__(self) -> str:
        return str(self.title)


class Comments(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True)
    likes = models.IntegerField(default=0, null=True)

    def __str__(self) -> str:
        return str(self.description)

class Likes(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return str(self.user)