from django.shortcuts import render, redirect
from blog.models import Post, Comment
from users.models import Profile


# Create your views here.

def posts_func(request):
    posts = Post.objects.filter(author__is_active=True, author__type='public', is_active=True)
    return render(request, 'posts_list.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        body = request.POST.get('body')
        if body and request.user.is_authenticated:
            Comment.objects.create(
                post=post,
                user=Profile.objects.get(user=request.user),
                body=body
            )
            return redirect("post_detail", slug=slug)
    comments = Comment.objects.filter(post=post, is_active=True).order_by('-date_added')
    return render(request, 'post_detail.html', {'post':post, 'comments':comments})
