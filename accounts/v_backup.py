# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from allauth.socialaccount.providers.oauth2.client import OAuth2Client
# from dj_rest_auth.registration.views import SocialLoginView
# from django.contrib.auth import authenticate
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken
# from accounts.error_render import UserErrorRender
# from accounts.serializers_backup import GetUserSerializer, RegisterModelSerializer, LoginModelSerializer




# class GoogleLoginViews(SocialLoginView):
#     adapter_class = GoogleOAuth2Adapter
#     callback_url = "http://localhost:5173"
#     client_class = OAuth2Client

# class GetUser(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self, request):
#         serializer = GetUserSerializer(request.user)
#         return Response({'user': serializer.data}, status=status.HTTP_200_OK)
    

# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)

#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }


# class UserRegistraionViews(APIView):
#     renderer_classes = [UserErrorRender]
#     def post(self, request):
#         serializer = RegisterModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Registration Successful.'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class UserLoginViews(APIView):
#     renderer_classes = [UserErrorRender]
#     def post(self, request):
#         serializer = LoginModelSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.data.get('email')
#             password = serializer.data.get('password')
#             user = authenticate(email=email, password=password)
#             if user:
#                 token = get_tokens_for_user(user=user)
#                 return Response({'Token':token, 'msg':'Login successful.'}, status=status.HTTP_200_OK)
#             return Response({'errors' : {'non_field_errors' : ["Email or password isn't valid."]}}, status=status.HTTP_404_NOT_FOUND)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
















# # from accounts.serializers import TokenSerializer
# # from rest_framework.authentication import TokenAuthentication
# # from allauth.socialaccount.models import SocialAccount
# # from rest_framework.authtoken.models import Token
# # from accounts.models import User



# # class GoogleLoginViews(SocialLoginView):
#     # adapter_class = GoogleOAuth2Adapter
#     # callback_url = "http://localhost:5173/api/auth/callback/google"
#     # client_class = OAuth2Client

#     # def post(self, request, *args, **kwargs):
#     #     request.data["id_token"] = request.data.get("access_token")
#     #     print(request.data)
#     #     return super().post(request, *args, **kwargs)
    
#     # def get(self, request, token):
#     #     user = User.objects.filter(username=request.user)
#     #     print(request.user)
#     #     return Response({'msg': 'token is', 'username': user}, status=status.HTTP_200_OK)
#     # def get(self, request, token):
#     #     token_key = Token.objects.filter(key=token)
#     #     for user_ in token_key:
#     #         serializer = TokenSerializer(instance=user_)
#     #         user = User.objects.get(id=serializer.data['user'])
#     #         return Response({'msg': 'token is', 'username': user.username, 'userToken': serializer.data['key']}, status=status.HTTP_200_OK)
#     #     return Response({'msg': 'unknown'}, status=status.HTTP_400_BAD_REQUEST)