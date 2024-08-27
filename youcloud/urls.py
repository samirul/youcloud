from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("audio/", include('api.urls')),
    path("api/auth/", include('dj_rest_auth.urls')),
    path("password-reset/confirm/<uidb64>/<token>/", TemplateView.as_view(template_name="account/email/password_reset_confirm.html"), name='password_reset_confirm'),
    path('api/registration/', include('dj_rest_auth.registration.urls')),
    path("api/social/login/", include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
