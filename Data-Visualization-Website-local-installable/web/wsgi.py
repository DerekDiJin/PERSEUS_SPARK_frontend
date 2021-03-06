"""
WSGI config for web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")

# Bootstrap WSGI application
application = get_wsgi_application()

# Boostrap Redis client
# TODO: disabled for local runnable
# from app.services.redis_manager import bootstrap
# bootstrap()
