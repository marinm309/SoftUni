from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(UserFollowers)
admin.site.register(UserFollowing)