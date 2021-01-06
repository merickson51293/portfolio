from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context={
        "blogs":Blog.objects.all()
    }
    return render(request, "index.html", context)

def blog(request):
    context={
        "blogs":Blog.objects.all()
    }
    return render(request, "blog.html", context)

def blog_post(request, blog_id):
    context={
        "blogs":Blog.objects.get(id=blog_id)
    }
    return render(request, "blog_post.html", context)

    