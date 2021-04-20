from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from . import viewsets


router = DefaultRouter()
# router.register(r'banners', viewsets.BannerViewSet)

urlpatterns = [
    path('posts/', views.PostViewListCreate.as_view()),
    path('posts/<int:pk>', views.PostViewDetailUpdateDelete.as_view()),
    path('posts/most-vieweds/', views.posts_most_vieweds),

    path('pages/', views.PageViewListCreate.as_view()),
    path('pages/<int:pk>', views.PageViewDetailUpdateDelete.as_view()),


    path('banners/', views.BannerViewListCreate.as_view()),
    path('banners/<int:pk>/', views.BannerViewDetailUpdateDelete.as_view()),

    path('banners/<int:pk>/up-sorter', views.up_order_banner),
    path('banners/<int:pk>/down-sorter', views.down_order_banner),

    path('banners/<int:pk>/click', views.click_banner),

    path('send-mail/', views.send_contact_form)
]  # + router.urls
