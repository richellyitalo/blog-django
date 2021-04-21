from django.shortcuts import render
from rest_framework import generics

from core.models import Post
from core.serializers import PostSerializer


class PostList(generics.ListAPIView):
    queryset = Post
    serializer = PostSerializer