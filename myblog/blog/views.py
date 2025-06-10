from django.shortcuts import render
from .models import Post
# Create your views here.


def post_list(request):
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'blog/home.html', {'posts': posts})

def places(request):
    return render(request, 'blog/.html')

def signIn(request):
    return render(request, 'blog/signIn.html')

def rooms(request):
    return render(request, 'blog/rooms.html')