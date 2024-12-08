"""
WSGI config for myApps project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# Add your project directory to the Python path
sys.path.append('/home/abhinavdewa65/ChefMind/recipe-app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myApps.settings')

application = get_wsgi_application()
