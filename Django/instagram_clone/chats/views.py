from django.http import JsonResponse
from django.shortcuts import render
from users.models import *
from posts.models import *
from django.http import JsonResponse

def inbox(request):
    user = request.user.profile
    friends = UserFollowers.objects.filter(user=user)
    active = True
    context = {'friends': friends, 'user': user, 'active': active}
    return render(request, 'chats/inbox.html', context)

def active_chat(request, pk):
    user = request.user.profile
    chat_with = Profile.objects.get(id=pk)
    active = False
    return JsonResponse({'active': active, 'chat_with': chat_with.id})
