from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'email',
            'username'
        )


class PostSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = (
            'title',
            'excerpt',
            'content',
            'image',
            'created_at',
            'updated_at',
            'owner'
        )