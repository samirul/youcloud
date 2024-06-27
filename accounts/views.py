from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.authtoken.models import Token
# from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.response import Response

# from allauth.socialaccount.models import SocialAccount
from accounts.models import User

# from accounts.serializers import TokenSerializer

from accounts.serializers import GetUserSerializer

class GoogleLoginViews(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:5173/api/auth/callback/google"
    client_class = OAuth2Client

    def post(self, request, *args, **kwargs):
        request.data["id_token"] = request.data.get("access_token")
        print(request.data)
        return super().post(request, *args, **kwargs)
    
    # def get(self, request, token):
    #     user = User.objects.filter(username=request.user)
    #     print(request.user)
    #     return Response({'msg': 'token is', 'username': user}, status=status.HTTP_200_OK)
    # def get(self, request, token):
    #     token_key = Token.objects.filter(key=token)
    #     for user_ in token_key:
    #         serializer = TokenSerializer(instance=user_)
    #         user = User.objects.get(id=serializer.data['user'])
    #         return Response({'msg': 'token is', 'username': user.username, 'userToken': serializer.data['key']}, status=status.HTTP_200_OK)
    #     return Response({'msg': 'unknown'}, status=status.HTTP_400_BAD_REQUEST)
    
class GetUser(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = GetUserSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)

    