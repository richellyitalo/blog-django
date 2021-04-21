from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from . import viewsets

router = DefaultRouter()
router.register(r'posts', viewsets.PostViewSet, basename='posts')
router.register(r'pages', viewsets.PageViewSet, basename='pages')
router.register(r'banners', viewsets.BannerViewSet, basename='banners')

urlpatterns = [    
    path('send-mail/', views.send_contact_form)
] + router.urls
# urlpatterns = [
#     path('posts/', views.PostList.as_view())
# ]
