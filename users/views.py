from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from blog.models import Post
from .forms import SignUpForm, SignInForm
from .models import Profile

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # email = request.POST.get('email')
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('/sign_up')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('/sign_up')
        # if User.objects.filter(email=email).exists():
        #     messages.error(request, 'Email in user')
        #     return redirect('/sign_up')
        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name
            # email=email
        )
        user.set_password(password)
        user.save()
        Profile.objects.create(user=user)
        login(request, user)
        return redirect('/')
    return render(request, 'sign_up.html')


def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                messages.error(request, 'Username or password is incorrect')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'sign_in.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('sign_in')


def profile_view(request, user):
    user = User.objects.get(username=user)
    profile = user.profile
    posts = Post.objects.filter(author=user).order_by("-date")

    is_following = False
    if request.user.is_authenticated:
        is_following = request.user in profile.followers.all()

    return render(request, "profile.html", {
        "profile": profile,
        "posts": posts,
        "is_following": is_following,
    })