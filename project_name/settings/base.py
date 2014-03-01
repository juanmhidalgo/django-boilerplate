"""
Django settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

from os.path import abspath, dirname, join, normpath
from sys import path
import os
import {{ project_name }} as project_module

PROJECT_ROOT = os.path.dirname(os.path.realpath(project_module.__file__))

########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = PROJECT_ROOT

# Site name:
SITE_NAME = '{{ project_name }}'

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION

########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#admins
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## DATABASE CONFIGURATION
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(BASE_DIR, 'db.sqlite3')),
    }
}
########## END DATABASE CONFIGURATION


# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/

# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#use-tz
USE_TZ = True

# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#site-id
SITE_ID = 1

########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#media-root
MEDIA_ROOT = normpath(join(PROJECT_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION

########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#static-root
STATIC_ROOT = normpath(join(PROJECT_ROOT, 'static'))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(PROJECT_ROOT, 'assets')),
)

# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## END STATIC FILE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = '{{ secret_key }}'
########## END SECRET CONFIGURATION


########## SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []
########## END SITE CONFIGURATION


########## FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)
########## END FIXTURE CONFIGURATION


########## TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
)
########## END TEMPLATE CONFIGURATION

########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#root-urlconf
ROOT_URLCONF = '{{ project_name }}.urls'
########## END URL CONFIGURATION

########## APP CONFIGURATION
DJANGO_APPS = (
    # Admin panel and documentation:
    'django.contrib.admin',
    # 'django.contrib.admindocs',

    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    # 'django.contrib.humanize',

)

THIRD_PARTY_APPS = (
    # Database migration helpers:
    #'south',
)

# Apps specific for this project go here.
LOCAL_APPS = (
)

# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
########## END LOGGING CONFIGURATION


########## WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#wsgi-application
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'
########## END WSGI CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION
