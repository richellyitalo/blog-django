from rest_framework import viewsets

from .models import Banner
from .serializers import BannerSerializer
from core.paginations import PublicPagination


class PublicViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = ()
    pagination_class = PublicPagination


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
