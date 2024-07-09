import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
from database.database import DATABASES # imported database # pylint: disable=unused-import


load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    
]

APPS = [
    "BaseId.apps.BaseidConfig",
    "api.apps.ApiConfig",
    "accounts.apps.AccountsConfig",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    "rest_framework.authtoken",
    "corsheaders",
    "django.contrib.sites",
    "django_celery_results",


    # Social Authentication

    "dj_rest_auth",
    "dj_rest_auth.registration",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google"

]

INSTALLED_APPS += APPS
INSTALLED_APPS += THIRD_PARTY_APPS

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "youcloud.urls"

SITE_ID = 1
REST_USE_JWT = True #  For Using Json Web Token


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "youcloud.wsgi.application"

# Custom User Model

AUTH_USER_MODEL = 'accounts.User'



# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = "static/"
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]



# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Email configuration

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_USE_TLS = True


# Celery Settings

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL_LINK')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = os.environ.get('CELERY_TIMEZONE_PLACE')

CELERY_RESULT_BACKEND = 'django-db'

# Simple JWT

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,

    'ALGORITHM': 'HS256',
    "SIGNING_KEY": os.environ.get('DJANGO_SIGNING_KEY'),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,


    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',
}



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    )
    
}






SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin-allow-popups"


REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_HTTPONLY':False,
    'JWT_AUTH_COOKIE': 'access',
    'JWT_AUTH_REFRESH_COOKIE': 'refresh',
} 

SOCIALACCOUNT_ADAPTER = 'accounts.adapters.SocialAccountAdapter'

# AUTHENTICATION_BACKENDS = (
#     'allauth.account.auth_backends.AuthenticationBackend',
# )

# ACCOUNT_AUTHENTICATION_METHOD = "email"
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_LOGOUT_ON_GET = True
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "http://localhost:5173/"
# # SOCIALACCOUNT_STORE_TOKENS = True

# # # # SOCIALACCOUNT_ONLY = True


# REST_AUTH = {
#     'USE_JWT': True,
#     # # 'SESSION_LOGIN': True,
#     'JWT_AUTH_HTTPONLY':False,
#     'JWT_AUTH_COOKIE': 'access',
#     'JWT_AUTH_REFRESH_COOKIE': 'refresh',
# } 


# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#         # "rest_framework.authentication.TokenAuthentication",
#         "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
#     )
    
# }


# authentication classes

# REST_FRAMEWORK = {
#     # 'DEFAULT_PERMISSION_CLASSES': (
#     #     "rest_framework.permissions.IsAuthenticated",
#     # ),

#     "DEFAULT_AUTHENTICATION_CLASSES": (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#         # "rest_framework.authentication.BasicAuthentication",
#         # "rest_framework.authentication.SessionAuthentication",
#         # "rest_framework.authentication.TokenAuthentication",
#         "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
#     )

# }

# CORS_ORIGIN_ALLOW_ALL = True

# SITE_ID = 1
# REST_USE_JWT = True #  For Using Json Web Token
# USE_JWT = True #  For Using Json Web Token



# LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'handlers': {
#       'file': {
#          'level': 'DEBUG',
#          'class': 'logging.FileHandler',
#          'filename': '/tmp/debug.log',
#       },
#    },
#    'loggers': {
#       'django': {
#          'handlers': ['file'],
#          'level': 'DEBUG',
#          'propagate': True,
#       },
#    },
# }

# REST_AUTH_SERIALIZERS = {
#     'USER_DETAILS_SERIALIZER': 'accounts.serializers.UserModelSerializer'
# }