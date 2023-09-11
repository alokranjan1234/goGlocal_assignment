from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class UserProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'first_name': request.user.first_name,'user':request.user.last_name}
        return Response(content)

# Create your views here.
