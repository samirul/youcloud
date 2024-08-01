from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from accounts.serializers import GetUserSerializer




class GoogleLoginViews(SocialLoginView):
    '''
        Added Google Login Views for login with google with dj_rest_auth and all auth
    '''
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:5173"
    client_class = OAuth2Client

class GetUser(APIView):
    '''
        For fetching user or user information after login user 
    '''
    permission_classes = [IsAuthenticated]
    def get(self, request):
        '''
            will send GET request from frontend reactjs
        '''
        serializer = GetUserSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)
    
