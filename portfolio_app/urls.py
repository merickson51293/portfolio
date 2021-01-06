from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('blog', views.blog),
    path('blog_post/<int:blog_id>', views.blog_post),
    path('proj_page/<int:project_id>', views.proj_page)
]