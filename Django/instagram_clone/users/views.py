from re import U
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from posts.models import Post
from .models import *


def user_register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'users/register.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.object.get(username=username)
        except:
            pass
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    context = {}
    return render(request, 'users/login.html', context)


def profile(request, pk):
    user = request.user.profile
    profile = Profile.objects.get(username=pk)
    posts = Post.objects.filter(user=profile)
    
    context = {'posts': posts, 'user': user, 'profile': profile}
    return render(request, 'users/profile.html', context)

def edit_profile(request, pk):
    user = request.user.profile
    profile = Profile.objects.get(id=pk)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid:
            form.save()
            return redirect(f'/profile/{user.user}/')

    context = {'form': form, 'user': user}
    return render(request, 'users/edit_profile.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')

def search_results(request):
    user = request.user.profile
    profile = Profile.objects.get(id=user.id)
    user_followers = UserFollowers.objects.filter(follower=profile.user)
    lst = []
    key_word = ''
    for i in user_followers:
        lst.append(i.user)
    if request.method == 'POST':
        if len(request.POST) != 0:
            key_word = request.POST['search']
            profiles = Profile.objects.filter(username__contains=key_word)
            if len(profiles) != 0:
                match = True
        else:
            key_word = ''
            profiles = Profile.objects.filter(username__contains=key_word)
            if len(profiles) != 0:
                match = True
    else:
        print(key_word)
        profiles = Profile.objects.filter(username__contains=key_word)
        if len(profiles) != 0:
            match = True

    context = {'profiles': profiles, 'user': user, 'match': match, 'followers': user_followers, 'lst': lst}
    return render(request, 'users/search_result.html', context)


def follow(request, pk):
    user = request.user.profile
    to_follow = Profile.objects.get(id=pk)
    profile = Profile.objects.get(id=user.id)
    possible = UserFollowers.objects.filter(user=to_follow, follower=profile.user)
    if len(possible) == 0:
        UserFollowers.objects.create(user=to_follow, follower=profile.user)
    return redirect(request.META['HTTP_REFERER'])

def unfollow(request, pk):
    user = request.user.profile
    to_unfollow = Profile.objects.get(id=pk)
    profile = Profile.objects.get(id=user.id)
    possible = UserFollowers.objects.filter(user=to_unfollow, follower=profile.user)
    if len(possible) != 0:
        form = UserFollowers.objects.get(user=to_unfollow, follower=profile.user)
        form.delete()
    return redirect(request.META['HTTP_REFERER'])
