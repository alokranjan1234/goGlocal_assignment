from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        access_token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        print('access_token',access_token)
        access_obj = AccessToken(token=access_token)
        user_id=access_obj['user_id']
        user = User.objects.get(id=user_id)
        setattr(request,'user',user)
        response = self.get_response(request)
        return response