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
    views = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'slug',
            'excerpt',
            'content',
            'image',
            'views',
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
            'slug',
            'content',
            'image'
        )


class BannerSerializer(serializers.ModelSerializer):
    sort_order = serializers.ReadOnlyField()
    class Meta:
        model = Banner
        exclude = ['clicks', ]


class BannerSerializerUpdate(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    class Meta:
        model = Banner
        exclude = ['sort_order', ]


""" Contact form """
class ContactMail(serializers.Serializer):
    subject = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    message = serializers.CharField(max_length=1000)
