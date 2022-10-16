from rest_framework import serializers
from .models import Urls


class UrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urls
        # fields = '__all__'
        fields = ['host_url', 'short_url']
