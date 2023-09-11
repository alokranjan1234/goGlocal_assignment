from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class UserProfileView(APIView):

    permission_classes = (IsAuthenticated,) # Permission class to check if user is authenticated

    def get(self, request):
        content = {'first_name': request.user.first_name,'last_name':request.user.last_name}
        return Response(content)

# Create your views here.
