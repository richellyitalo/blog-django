from django.urls import path

from .views import PostViewListCreate, PostViewDetailUpdateDelete


urlpatterns = [
    path('posts/', PostViewListCreate.as_view()),
    path('posts/<int:pk>', PostViewDetailUpdateDelete.as_view()),
]
