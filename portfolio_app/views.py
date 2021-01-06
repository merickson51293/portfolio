from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context={
        "blogs":Blog.objects.all(),
        "project":Project.objects.all()
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

def proj_page(request, project_id):
    context={
        "project":Project.objects.get(id=project_id)
    }
    return render(request, "proj_page.html", context)