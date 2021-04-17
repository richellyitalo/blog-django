from django.shortcuts import render
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, serializers
from rest_framework import generics


from .serializers import PostSerializer
from .models import Post


class PostViewListCreate(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostViewDetailUpdateDelete(mixins.RetrieveModelMixin,
                                 mixins.DestroyModelMixin,
                                 mixins.UpdateModelMixin,
                                 generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # update parcial
        # return self.update(request, *args, **kwargs)
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'oi': "teste"})

    def post(self, request, *args, **kwargs):
        return Response(request.data)
