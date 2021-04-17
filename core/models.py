from django.db import models
from django.db.models.signals import post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
import os


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
    owner = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Page(TimestampableMixin):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='image/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Post)
@receiver(post_delete, sender=Page)
def handler_delete_image(sender, instance, **kwargs):
    os.remove(instance.image.path)
