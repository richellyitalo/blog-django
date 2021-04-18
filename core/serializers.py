from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Post, Page, Banner


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
            'id',
            'title',
            'excerpt',
            'content',
            'image',
            'created_at',
            'updated_at',
            'owner'
        )


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = (
            'id',
            'title',
            'content',
            'image'
        )


class BannerSerializer(serializers.ModelSerializer):
    sort_order = serializers.ReadOnlyField()
    class Meta:
        model = Banner
        fields = '__all__'
        # exclude = ['sort_order', ]


class BannerSerializerUpdate(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    class Meta:
        model = Banner
        exclude = ['sort_order', ]
