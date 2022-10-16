from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import string
import json
from random import choice
from .models import Urls
from .serializers import UrlsSerializer


# Create your views here.

def validate(request):
    try:
        if request.data.get('host_url') \
                and not str(request.data.get('host_url')).startswith('http') \
                and not str(request.data.get('host_url')).startswith('ftp'):
            return {'error': "The host_url must start with 'http' or 'ftp'. Edit, please, and try again."}
        elif request.data.get('short_url') \
                and not str(request.data.get('short_url')).startswith('http') \
                and not str(request.data.get('short_url')).startswith('ftp'):
            return {'error': "The short_url must start with 'http' or 'ftp'. Edit, please, and try again."}
        elif request.data.get('length') \
                and int(request.data.get('length')) < 8:
            return {'error': "The length must be more then 7. Edit, please, and try again."}
        elif request.data.get('list_of_symbols') \
                and len(set(request.data.get('list_of_symbols'))) <= 10:
            return {'error': "The list_of_symbol has to consist of more then 10 different symbols. Edit, please, and try again."}
        else:
            return
    except:
        return {'error': "User data is not correct. Edit, please, and try again."}


class UrlAPIjson(APIView):
    serializer_class = UrlsSerializer

    def get(self, request):
        list_of_urls = Urls.objects.all()
        return Response(UrlsSerializer(list_of_urls, many=False).data)

    def post(self, request):
        data = {
            'info': "User's data in POST request:",
            'host_url': request.data.get('host_url'),
            'short_url': request.data.get('short_url'),
            'length': request.data.get('length'),
            'list_of_symbols': request.data.get('list_of_symbols'),
        }
        with open('rest-urls-log.json', 'a') as f:
            json.dump(data, f, indent=4)
            json.dump('.' * 40, f, indent=4)

        val = validate(request)
        if val:
            return Response(val)
        num_of_chars = request.data.get('length')
        if not num_of_chars:
            num_of_chars = 8
        else:
            num_of_chars = int(num_of_chars)
        list_of_symbols = request.data.get('list_of_symbols')
        if not list_of_symbols:
            list_of_symbols = string.ascii_letters + string.digits

        filter_by_host = request.data.get('host_url')
        data_host_url = Urls.objects.all().filter(host_url=filter_by_host)
        filter_by_short = request.data.get('short_url')
        data_short_url = Urls.objects.all().filter(short_url=filter_by_short)
        if data_host_url:
            return Response(UrlsSerializer(data_host_url, many=True).data)
        elif data_short_url:
            return Response({'error': "The short_url exists. Edit, please, and try again."})
        else:
            check_obj = True
            check_short_url = request.data.get('short_url')
            while check_obj:
                if check_short_url:
                    check_obj = Urls.objects.all().filter(short_url=check_short_url)
                else:
                    inx = request.data.get('host_url').find('/', 8)
                    host = request.data.get('host_url')[:inx + 1]
                    short = ''.join(choice(list_of_symbols) for _ in range(num_of_chars))
                    check_short_url = host + short
            instance = Urls.objects.create(
                host_url=request.data.get('host_url'),
                short_url=check_short_url,
            )
            serializer = UrlsSerializer(data=request.data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'post': serializer.data})

    def delete(self, request):
        instance = Urls.objects.all()
        instance.delete()
        return Response({'delete': "The db is empty."})

