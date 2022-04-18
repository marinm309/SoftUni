from django.shortcuts import redirect, render
from .forms import PostForm, CommentForm
from.models import Post, Likes, Comments, CommentLikes
from django.contrib.auth.decorators import login_required
from users.models import Profile, UserFollowers
import os

@login_required(login_url='login')
def home(request):
    user = request.user.profile
    following = UserFollowers.objects.filter(follower=user.user)
    lst = []
    for i in following:
        lst.append(i.user)
    posts = Post.objects.all()
    posts = Post.objects.order_by('-created')
    comments = Comments.objects.all()
    dic = {}
    for comment in comments:
        if comment.post not in dic:
            dic[comment.post] = [comment.description]
        else:
            dic[comment.post].append(comment.description)
    context = {'posts': posts, 'comments': comments, 'following': following, 'lst': lst, 'user': user, 'dic': dic}
    return render(request, 'posts/home.html', context)


@login_required(login_url='login')
def create_post(request):
    form = PostForm()
    user = request.user.profile
    profile = Profile.objects.get(user=user.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        extesion = os.path.splitext(str(request.FILES['file_upload']))[1]
        if form.is_valid:
            post = form.save(commit=False)
            post.user = user
            if extesion == '.mp4':
                post.post_type = 'video'
            else:
                post.post_type = 'photo'
            post.save()
            profile.total_posts += 1
            profile.save()
            return redirect('home')
    context = {'form': form, 'user': user}
    return render(request, 'posts/create_post.html', context)

@login_required(login_url='login')
def delete_post(request, pk):
    user = request.user.profile
    post = Post.objects.get(id=pk)
    profile = Profile.objects.get(user=user.user)
    profile.total_posts -= 1
    profile.save()
    post.delete()
    return redirect(f'/profile/{user.user}')

@login_required(login_url='login')
def edit_post(request, pk):
    user = request.user.profile
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid:
            form.save()
            return redirect(f'/profile/{user.user}')
    context = {'form': form}
    return render(request, 'posts/create_post.html', context)

@login_required(login_url='login')
def like_post(request, pk):
    user = request.user.profile
    post = Post.objects.get(id=pk)
    like = Likes.objects.filter(user=user, post=post)
    if len(like) == 0:
        like = Likes.objects.create(user=user, post=post)
        post.like += 1
        post.save()
    else:
        like = Likes.objects.get(user=user, post=post)
        like.delete()
        post.like -= 1
        post.save()

    return redirect(request.META['HTTP_REFERER'])

@login_required(login_url='login')
def create_comment(request, pk):
    user = request.user.profile
    post = Post.objects.get(id=pk)
    description = request.POST['comment']
    comment = Comments.objects.create(user=user, post=post, description=description)
    comment.save()
    post.num_of_comments += 1
    post.save()

    return redirect(request.META['HTTP_REFERER'])

@login_required(login_url='login')
def delete_comment(request, pk, ck):
    user = request.user.profile
    post = Post.objects.get(id=pk)
    post.num_of_comments -= 1
    post.save()
    comment = Comments.objects.get(id=ck)
    comment.delete()

    return redirect(request.META['HTTP_REFERER'])

@login_required(login_url='login')
def like_comment(request, pk):
    user = request.user.profile
    comment = Comments.objects.get(id=pk)
    like = CommentLikes.objects.filter(user=user, comment=comment)
    if len(like) == 0:
        like = CommentLikes.objects.create(user=user, comment=comment)
        comment.likes += 1
        comment.save()
    else:
        like = CommentLikes.objects.get(user=user, comment=comment)
        like.delete()
        comment.likes -= 1
        comment.save()
    return redirect(request.META['HTTP_REFERER'])

@login_required(login_url='login')
def single_post(request,pk):
    user = request.user.profile
    post = Post.objects.get(id=pk)
    comments = Comments.objects.filter(post=post)
    user_followers = UserFollowers.objects.filter(follower=user.user)
    lst = []
    for i in user_followers:
        lst.append(i.user)
    if len(comments) == 0:
        empty = True
    else:
        empty = False

    context = {'comments': comments, 'user': user, 'post': post, 'lst': lst, 'empty': empty}
    return render(request, 'posts/single_post.html', context)
