from time import time
from datetime import datetime
import json

from django.contrib.auth.models import AnonymousUser


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        user = str(request.user)
        now = str(datetime.now())
        data = {
            'user': user,
            'method': request.method,
            'url_path': request.path,
            'datetime': now,
        }
        with open('rest-urls-log.json', 'a') as f:
            json.dump(data, f, indent=4)
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response