from rest_framework import routers
from .api import UrlsViewSet
from django.urls import path, include

from .views import UrlAPIjson

router = routers.DefaultRouter()
router.register('api/urls', UrlsViewSet, 'url')

urlpatterns = router.urls
urlpatterns += [
    path('api/', UrlAPIjson.as_view(), name='GetPost'),
]
