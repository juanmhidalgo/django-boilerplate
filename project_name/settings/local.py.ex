"""Development settings and globals."""


from os.path import join, normpath

from {{project_name}}.settings.dev import *


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE' : 'django_mongodb_engine',
        'NAME': 'dev_{{ project_name }}',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
########## END DATABASE CONFIGURATION
