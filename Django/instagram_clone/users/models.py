from django.db import models
import uuid
from django.contrib.auth.models import User

class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.user)
