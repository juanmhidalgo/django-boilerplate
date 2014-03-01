"""
WSGI config for {{ project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.dev")

import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler()


def application(environ, start_response):
    if 'DJANGO_SETTINGS_MODULE' in environ:
        os.environ['DJANGO_SETTINGS_MODULE'] = environ['DJANGO_SETTINGS_MODULE']

    return _application(environ, start_response)
