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

@login_required(login_url='login')
def profile(request):
    form = ProfileForm()
    user_in = request.user.profile
    posts = Post.objects.filter(user=user_in)
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid:
            profile = form.save(commit=False)
            print(profile.user)
            profile.user = user_in
            profile.save()
            return redirect('profile')
    context = {'form': form, 'posts': posts}
    return render(request, 'users/profile.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')

def search_results(request):
    user = request.user.profile
    profile = Profile.objects.get(id=user.id)
    user_followers = UserFollowers.objects.filter(user=profile)
    if request.method == 'POST':
        key_word = request.POST['search']
        profiles = Profile.objects.filter(username__contains=key_word)
        if len(profiles) != 0:
            match = True

    context = {'profiles': profiles, 'user': user, 'match': match, 'followers': user_followers}
    return render(request, 'users/search_result.html', context)


def follow(request, pk):
    user = request.user.profile
    to_follow = Profile.objects.get(id=pk)
    profile = Profile.objects.get(id=user.id)
    possible = UserFollowers.objects.filter(user=to_follow, follower=profile.user)
    if len(possible) == 0:
        UserFollowers.objects.create(user=to_follow, follower=profile.user)
    return render(request, 'users/search_result.html')
