from django.urls import path

from .views import (
    PostViewListCreate,
    PostViewDetailUpdateDelete,
    PageViewListCreate
)


urlpatterns = [
    path('posts/', PostViewListCreate.as_view()),
    path('posts/<int:pk>', PostViewDetailUpdateDelete.as_view()),

    path('pages/', PageViewListCreate.as_view()),
]
