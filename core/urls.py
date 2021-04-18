from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    PostViewListCreate,
    PostViewDetailUpdateDelete,

    PageViewListCreate,
    PageViewDetailUpdateDelete,

    BannerViewListCreate,
    BannerViewDetailUpdateDelete
)
from . import viewsets


router = DefaultRouter()
# router.register(r'banners2', viewsets.BannerViewSet)

urlpatterns = [
    path('posts/', PostViewListCreate.as_view()),
    path('posts/<int:pk>', PostViewDetailUpdateDelete.as_view()),

    path('pages/', PageViewListCreate.as_view()),
    path('pages/<int:pk>', PageViewDetailUpdateDelete.as_view()),

    
    path('banners/', BannerViewListCreate.as_view()),
    path('banners/<int:pk>/', BannerViewDetailUpdateDelete.as_view()),
] #+ router.urls
