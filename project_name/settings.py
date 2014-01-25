"""Django settings module"""
from os import environ, path

DEBUG = TEMPLATE_DEBUG = environ.get('DJANGO_DEBUG', '0') == '1'
PROJECT_ROOT = environ.get('DJANGO_HOME', '')

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path.join(PROJECT_ROOT, 'default.db'),
    },
}

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

    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },

    'formatters': {
        'default': {
            'format': '%(asctime)s <%(name)s:%(levelname)s> %(message)s'
        },
        'debug': {
            'format': '%(asctime)s <%(name)s:%(levelname)s>'
                      ' [%(module)s:%(process)d:%(thread)d] %(message)s'
        },
    },

    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'default': {
            'level': 'DEBUG' if DEBUG else 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'debug' if DEBUG else 'default',
            'filename': path.join(PROJECT_ROOT, '{{ project_name }}.log'),
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },

    'loggers': {
        '{{ project_name }}': {
            'handlers': ['console', 'default'],
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
        'django': {
            'handlers': ['console', 'default'],
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'py.warnings': {
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
