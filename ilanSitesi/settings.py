from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '8CVgaUuCLMw481jkhlNwvi9VamWWZhu0CmFxMYDJFUne_nBGtHQTTV7aoQD1mdXGVGs'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'ilanlar',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ilanSitesi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ilanSitesi.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    import dj_database_url
    DATABASES['default'] = dj_database_url.parse(DATABASE_URL)

LANGUAGE_CODE = 'tr-tr'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_TRUSTED_ORIGINS = [
    'https://web-production-720eb3.up.railway.app',
    'https://seyfettin65.pythonanywhere.com',
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = TrueSESSION_COOKIE_AGE = 31536000  # 1 yıl
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# Google Cloud Storage
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'projem6565'
GS_CREDENTIALS = 'google-credentials.json'

# Google credentials from environment
import base64, json, os
from google.oauth2 import service_account

_creds_b64 = os.environ.get('GS_CREDENTIALS_BASE64')
if _creds_b64:
    _creds_b64_padded = _creds_b64 + '=' * (4 - len(_creds_b64) % 4)
    _creds_json = json.loads(base64.b64decode(_creds_b64_padded))
    GS_CREDENTIALS = service_account.Credentials.from_service_account_info(_creds_json)
