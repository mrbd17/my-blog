from django.shortcuts import render , redirect , get_object_or_404
from .models import Post,Comment
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreatePost,UpdatePost,CommentForm
# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request , f"!Wellcome {user.username}")
            return redirect("home")
        else:
            messages.error(request, "Username or password is not correct")
    form = AuthenticationForm
    return render(request, 'Authentication/login.html',{"form":form})
@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request,'You have been logged our successfully')
        return redirect("login")
    return render(request)
            
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm
    return render(request,"Authentication/register.html",{'form':form})
def post_detail(request , post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request,'blog/post_detail.html',{"post":post} )
def home(request):
    post = Post.objects.all()
    return render(request, 'blog/home.html',{"post":post})
@login_required
def create_post(request):
    if request.method == 'POST':
       form = CreatePost(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect('home')
    else:
        form = CreatePost
    return render(request, 'blog/post_create.html', {"form":form} )

@login_required
def update_post(request , post_id):
    post = get_object_or_404(Post, id=post_id)
    form = UpdatePost(request.POST , request.FILES,instance=post)
    if request.user != post.author:
        return HttpResponse("You are not allowed here")
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"post":post,"form":form}
    return render(request,'blog/post_update.html', context)
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return HttpResponse("You are not allowed here")
    if request.method == 'POST':
        post.delete()
        return redirect("home")
    return render(request, {"obj":post})

@login_required
def comment_view(request , post_id):
    post = get_object_or_404(Post,id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.author = request.author
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'blog/add_comment.html',{"form":form})