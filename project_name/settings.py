"""Django settings module"""
import os


ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED', 'localhost,127.0.0.1,::1').split(',')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = TEMPLATE_DEBUG = os.environ.get('DJANGO_DEBUG', '1').lower() not in ('0', 'f', 'false')
HOME_DIR = os.environ.get('DJANGO_HOME', 'run')
SECRET_KEY = os.environ.get('DJANGO_SECRET', '{{ secret_key }}')


ROOT_URLCONF = 'project_name.urls'
MEDIA_ROOT = os.path.join(HOME_DIR, 'media')
MEDIA_URL = '/project_name/media/'
STATIC_ROOT = os.path.join(HOME_DIR, 'static')
STATIC_URL = '/project_name/static/'

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en-us'

USE_TZ = True
TIME_ZONE = 'UTC'


ADMINS = [('admin', 'root')]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' \
    if DEBUG else 'django.core.mail.backends.smtp.EmailBackend'


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'project_name.main',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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

WSGI_APPLICATION = 'project_name.wsgi.application'


# Load local settings
try:
    from project_name.localsettings import *
except ImportError:
    pass
