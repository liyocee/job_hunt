from django import http
from django.conf import settings


class CORSMiddleware(object):
    """
       ALLOW CORS
    """
    CORS_ALLOWED_ORIGINS = settings.CLIENT_ORIGIN
    CORS_ALLOWED_METHODS = ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE', 'PATCH']
    CORS_ALLOWED_HEADERS = ['Content-Type', 'X-CSRFToken']

    def process_request(self, request):

        if 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
            response = http.HttpResponse()
            response['Access-Control-Allow-Origin'] = self.CORS_ALLOWED_ORIGINS
            allowed_methods = ",".join(self.CORS_ALLOWED_METHODS)
            allowed_headers = ",".join(self.CORS_ALLOWED_HEADERS)
            response['Access-Control-Allow-Methods'] = allowed_methods
            response['Access-Control-Allow-Headers'] = allowed_headers
            response['Access-Control-Allow-Credentials'] = 'true'

            return response

        return None

    def process_response(self, request, response):
        if response.has_header('Access-Control-Allow-Origin'):
            return response
        origin = request.META.get('HTTP_ORIGIN', self.CORS_ALLOWED_ORIGINS)
        response['Access-Control-Allow-Origin'] = origin
        allowed_methods = ",".join(self.CORS_ALLOWED_METHODS)
        allowed_headers = ",".join(self.CORS_ALLOWED_HEADERS)
        response['Access-Control-Allow-Methods'] = allowed_methods
        response['Access-Control-Allow-Headers'] = allowed_headers
        response['Access-Control-Allow-Credentials'] = 'true'
        return response
