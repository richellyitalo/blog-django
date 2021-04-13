from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=150)
    content = models.TextField()
    image = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
