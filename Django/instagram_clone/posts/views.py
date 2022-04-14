from turtle import pos
from django.shortcuts import redirect, render
from pkg_resources import ResolutionError
from .forms import PostForm, CommentForm
from.models import Post, Likes, Comments
from django.contrib.auth.decorators import login_required
from users.models import UserFollowers

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
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.user = user
            post.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'posts/create_post.html', context)

def delete_post(request, pk):
    user = request.user.profile
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect(f'/profile/{user.user}')

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

def create_comment(request, pk):
    user = request.user.profile
    post = Post.objects.get(id=pk)
    description = request.POST['comment']
    comment = Comments.objects.create(user=user, post=post, description=description)
    comment.save()
    post.num_of_comments += 1
    post.save()

    return redirect(request.META['HTTP_REFERER'])

def single_post(request,pk):
    user = request.user.profile
    post = Post.objects.get(id=pk)
    comments = Comments.objects.filter(post=post)
    user_followers = UserFollowers.objects.filter(follower=user.user)
    lst = []
    for i in user_followers:
        lst.append(i.user)
    context = {'comments': comments, 'useer': user, 'post': post, 'lst': lst}
    return render(request, 'posts/single_post.html', context)
