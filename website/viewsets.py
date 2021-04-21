from rest_framework import viewsets, pagination
from rest_framework.response import Response

from core.models import Post
from core.serializers import PostSerializer
from core.viewsets import PublicViewset


class PostViewSet(PublicViewset):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def retrieve(self, request, pk=None):
        post = self.get_object()
        serializer = self.get_serializer(post)
        post.add_view()
        return Response(serializer.data)
