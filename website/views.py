from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import generics, pagination, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from core.models import Post
from core.serializers import PostSerializer, ContactMail


class PublicPagination(pagination.LimitOffsetPagination):
    default_limit = 12


class PublicRoute(generics.GenericAPIView):
    permission_classes = []
    pagination_class = PublicPagination


class PostList(PublicRoute, generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


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
