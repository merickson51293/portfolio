from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.title}"

class Project(models.Model):
    name = models.CharField(max_length=100)
    short_des = models.CharField(max_length=255)
    tech_used = models.CharField(max_length=400)
    description = models.TextField()
    picture=models.ImageField(upload_to ='img/')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name}"
