from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)

class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    author = models.ForeignKey(User)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
