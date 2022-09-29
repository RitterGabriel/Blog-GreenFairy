from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def post(request, post_pk):
    posts = get_object_or_404(Post, pk=post_pk)
    return render(request, 'post.html', {'post': posts})

def politic(request):
    posts = Post.objects.all().filter(category='1')
    return render(request, 'home.html',
                  {'posts': posts})

def sport(request):
    posts = Post.objects.all().filter(category='2')
    return render(request, 'home.html',
                  {'posts': posts})

def tech(request):
    posts = Post.objects.all().filter(category='3')
    return render(request, 'home.html',
                  {'posts': posts})