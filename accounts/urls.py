from django.urls import path, include

from accounts.views import GoogleLoginViews

urlpatterns = [
    path("google/", GoogleLoginViews.as_view(), name='google'),
    path('accounts/', include('allauth.urls')),
    path('user/<str:token>/', GoogleLoginViews.as_view(), name='user'),
    
]
