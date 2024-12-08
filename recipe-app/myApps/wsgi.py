"""
WSGI config for myApps project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

path = '/ChefMind/recipe-app'
if path not in sys.path:
 sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'allinone.settings'
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myApps.settings')

application = get_wsgi_application()
