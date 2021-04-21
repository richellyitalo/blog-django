from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from . import viewsets

router = DefaultRouter()
router.register(r'posts', viewsets.PostViewSet, basename='posts')

urlpatterns = router.urls

# urlpatterns = [
#     path('posts/', views.PostList.as_view())
# ]
