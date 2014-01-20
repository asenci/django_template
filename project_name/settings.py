"""Django settings module"""
from os import environ, path

PROJECT_ROOT = environ.get('DJANGO_HOME', '')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path.join(PROJECT_ROOT, 'default.db'),
    },
}

DEBUG = TEMPLATE_DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_SUBJECT_PREFIX = '[{{ project_name }}] '

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    '{{ project_name }}.main',
)

LANGUAGE_CODE = 'pt-br'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'formatters': {
        'default': {
            'format': '%(asctime)s <%(name)s:%(levelname)s> %(message)s'
        },
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
    },

    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'py.warnings': {
            'handlers': ['console'],
        },
        'spyne': {
            'handlers': ['console'],
        },
    },
}

MEDIA_ROOT = path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'

ROOT_URLCONF = '{{ project_name }}.main.urls'

SECRET_KEY = '{{ secret_key }}'

STATIC_ROOT = path.join(PROJECT_ROOT, 'static')

STATIC_URL = '/static/'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True
