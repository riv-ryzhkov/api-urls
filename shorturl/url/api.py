from .models import Urls
from rest_framework import viewsets, permissions
from .serializers import UrlsSerializer


class UrlsViewSet(viewsets.ModelViewSet):
    queryset = Urls.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UrlsSerializer