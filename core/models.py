from django.db import models
from django.contrib.auth.models import User


class TimestampableMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Post(TimestampableMixin):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to='image/%Y/%m/%d/', blank=True)
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
