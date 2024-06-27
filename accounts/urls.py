from django.urls import path, include

from accounts.views import GoogleLoginViews, GetUser

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("google/", GoogleLoginViews.as_view(), name='google'),
    path('accounts/', include('allauth.urls')),
    path('user/<str:token>/', GoogleLoginViews.as_view(), name='user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', GetUser.as_view(), name='get_user'),
    
]
