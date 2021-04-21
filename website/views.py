from django.shortcuts import render
from rest_framework import generics
from rest_framework import pagination

from core.models import Post
from core.serializers import PostSerializer


class PublicPagination(pagination.LimitOffsetPagination):
    default_limit = 12


class PublicRoute(generics.GenericAPIView):
    permission_classes = []
    pagination_class = PublicPagination


class PostList(PublicRoute, generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
