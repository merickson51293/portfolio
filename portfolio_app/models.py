from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    short_des = models.CharField(max_length=255)
    tech_used = models.CharField(max_length=400)
    description = models.TextField()
    picture=models.ImageField(upload_to ='img/')
    link=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name}"

class Blog(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    proj_blog = models.ForeignKey(Project, related_name="project_blog", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.title}"