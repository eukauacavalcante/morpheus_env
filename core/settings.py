import os
from datetime import timedelta
from pathlib import Path

from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'axes',

    'users',
    'tools',
    'notifications',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'axes.middleware.AxesMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['core/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configurações de Login e Signin
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesStandaloneBackend',
    'django.contrib.auth.backends.ModelBackend',
]
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'
AXES_ENABLED = True
AXES_ENABLE_ADMIN = True
AXES_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = timedelta(minutes=10)
AXES_LOCKOUT_PARAMETERS = ['username', 'ip_address']
AXES_LOCKOUT_CALLABLE = 'users.views.custom_lockout'

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AI Config
AI_MODE = False
API_KEY = config('API_KEY')
AI_MODEL = config('AI_MODEL')

# E-mail functions
EMAIL_MODE = False # To do: se falso, imprime apenas no console

# E-mail Config
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

# OAuth2 Google Config
GOOGLE_OAUTH2_CLIENT_ID = config('GOOGLE_OAUTH2_CLIENT_ID')
GOOGLE_OAUTH2_CLIENT_SECRET = config('GOOGLE_OAUTH2_CLIENT_SECRET')
GOOGLE_OAUTH2_REFRESH_TOKEN = config('GOOGLE_OAUTH2_REFRESH_TOKEN')

JAZZMIN_SETTINGS = {
    "site_title": "Morpheus Env",
    "site_header": "Morpheus Env",
    "site_brand": "Morpheus Env",
    "site_logo_classes": "img-circle",
    "welcome_sign": "Bem-vindo ao Morpheus Env Admin!",
    "copyright": "Kauã Cavalcante",
    "show_sidebar": True,
    "navigation_expanded": True,
    "order_with_respect_to": ["auth",],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "axes.accessattempt": "fa-solid fa-folder-open",
        "axes.accesslog": "fa-solid fa-circle-check",
        "axes.accessfailurelog": "fa-solid fa-triangle-exclamation",
        "users.TermsOfUseAndPrivacyPolicy": "fa-solid fa-file-lines",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "use_google_fonts_cdn": True,
    "show_ui_builder": True,
}
