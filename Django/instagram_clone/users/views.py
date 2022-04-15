from re import U
from turtle import pos
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from posts.models import Post
from .models import *
from .forms import CustomUserCreationForm


def user_register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')
        else:
            return redirect('register')
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
    total_posts = len(posts)
    followers = UserFollowers.objects.filter(user=profile)
    total_followers = len(followers)
    following = UserFollowers.objects.filter(follower=profile.user)
    total_following = len(following)
    user_followers = UserFollowers.objects.filter(follower=user.user)
    lst = []
    for i in user_followers:
        lst.append(i.user)
    context = {'posts': posts, 'user': user, 'profile': profile, 'total_posts': total_posts, 'total_followers': total_followers, 'total_following': total_following, 'lst': lst}
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
    return redirect('login')

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
                match = False
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
    to_follow.total_followers += 1
    to_follow.save()
    profile.total_following += 1
    profile.save()
    possible = UserFollowers.objects.filter(user=to_follow, follower=profile.user)
    if len(possible) == 0:
        UserFollowers.objects.create(user=to_follow, follower=profile.user)
    return redirect(request.META['HTTP_REFERER'])

def unfollow(request, pk):
    user = request.user.profile
    to_unfollow = Profile.objects.get(id=pk)
    profile = Profile.objects.get(id=user.id)
    to_unfollow.total_followers -= 1
    to_unfollow.save()
    profile.total_following -= 1
    profile.save()
    possible = UserFollowers.objects.filter(user=to_unfollow, follower=profile.user)
    if len(possible) != 0:
        form = UserFollowers.objects.get(user=to_unfollow, follower=profile.user)
        form.delete()
    return redirect(request.META['HTTP_REFERER'])


def view_followers(request, pk):
    user = request.user.profile
    profile = Profile.objects.get(username=pk)
    followers = UserFollowers.objects.filter(user=profile)
    following = UserFollowers.objects.filter(follower=user.user)
    total_followers = len(followers)
    following_lst = []
    for i in following:
        following_lst.append(i.user.username)
    context = {'followers': followers, 'following_lst': following_lst, 'user': user, 'profile': profile, 'total_followers': total_followers}
    return render(request, 'users/view_followers.html', context)


def view_following(request, pk):
    user = request.user.profile
    profile = Profile.objects.get(username=pk)
    followers = UserFollowers.objects.filter(follower=user.user)
    following = UserFollowers.objects.filter(follower=profile.user)
    total_following = len(following)
    following_lst = []
    for i in followers:
        following_lst.append(i.user.username)
    print(following_lst)
    context = {'user': user, 'profile': profile, 'following_lst': following_lst, 'following': following, 'total_following': total_following}
    return render(request, 'users/view_following.html', context)

