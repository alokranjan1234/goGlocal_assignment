from django.contrib.auth.models import User
from rest_framework_simplejwt import authentication
from django.contrib.auth.middleware import AuthenticationMiddleware


class AuthMiddleware(AuthenticationMiddleware):
    '''
    AuthMidddleware to set user attribute in request
    '''

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_request(self, request, view_func, view_args, view_kwargs):
        request.user = authentication.JWTAuthentication().authenticate(request)[0]