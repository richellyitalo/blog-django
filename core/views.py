from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, serializers, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication, TokenAuthentication
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    BasePermission,
    SAFE_METHODS
)

from .auth import BearerAuthentication

from .serializers import (
    PostSerializer,
    PageSerializer,
    BannerSerializer,
    BannerSerializerUpdate,
    ContactMail
)
from .models import Post, Page, Banner


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


'''
Post view
'''


class PostViewListCreate(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

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
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post.add_view()
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # update parcial
        # return self.partial_update(request, *args, **kwargs)
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


'''
Page view
'''


class PageViewListCreate(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         generics.GenericAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PageViewDetailUpdateDelete(mixins.RetrieveModelMixin,
                                 mixins.UpdateModelMixin,
                                 mixins.DestroyModelMixin,
                                 generics.GenericAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


'''
Banner view
'''


class BannerViewListCreate(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           generics.GenericAPIView):

    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BannerViewDetailUpdateDelete(mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   generics.GenericAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)


""" Banners: register click banner """


@api_view(['GET'])
@permission_classes(())
def click_banner(request, pk):
    try:
        banner = Banner.objects.get(pk=pk)
        if banner.url in (None, ""):
            return Response({"message": "Banner not has url"}, status=status.HTTP_404_NOT_FOUND)
        banner.add_click()
        return Response({"url": banner.url, "new_window": banner.new_tab})
    except Banner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


""" Banners: set order """


@api_view(['PATCH'])
def up_order_banner(request, pk):
    try:
        banner = Banner.objects.get(pk=pk)
    except Banner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if banner.sort_order == 1:
        return Response(BannerSerializer(banner).data)

    qs = Banner.objects.filter(
        sort_order__lt=banner.sort_order).order_by('-sort_order')[:1]
    if qs.exists():
        banner_destination = qs.get()
        new_sorter_order = banner_destination.sort_order
        banner_destination.sort_order = banner.sort_order
        banner_destination.save()

        banner.sort_order = new_sorter_order
        banner.save()

    return Response(BannerSerializer(banner).data)


@api_view(['PATCH'])
def down_order_banner(request, pk):
    try:
        banner = Banner.objects.get(pk=pk)
    except Banner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    qs = Banner.objects.filter(
        sort_order__gt=banner.sort_order).order_by('sort_order')[:1]
    if qs.exists():
        banner_destination = qs.get()
        new_sorter_order = banner_destination.sort_order
        banner_destination.sort_order = banner.sort_order
        banner_destination.save()

        banner.sort_order = new_sorter_order
        banner.save()

    return Response(BannerSerializer(banner).data)


@api_view(['POST'])
@permission_classes(())
def send_contact_form(request):
    serializer = ContactMail(data=request.data)
    if serializer.is_valid():
        send_mail(
            "Contact form " + serializer.validated_data['subject'],
            serializer.validated_data['message'],
            serializer.validated_data['email'],
            [settings.EMAIL_CONTACT],
            html_message=serializer.validated_data['message'],
            fail_silently=False,
        )

        return Response({'message': 'Mail sent'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
